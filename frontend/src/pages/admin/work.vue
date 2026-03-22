<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import DataTable from '@/components/admin/DataTable.vue'
import ConfirmModal from '@/components/admin/ConfirmModal.vue'
import WorkForm from '@/components/admin/forms/WorkForm.vue'
import { useAPI } from '@/composables/useAPI'

const { get, post, put, del } = useAPI()

const work = ref<any[]>([])
const loading = ref(false)
const showForm = ref(false)
const showConfirm = ref(false)
const editing = ref<any>(null)
const deleting = ref<any>(null)

const columns = [
  { key: 'position', label: 'Position' },
  { key: 'company',  label: 'Company' },
  { key: 'join_date', label: 'From' },
  { key: 'resignation_date', label: 'To' },
  { key: 'place', label: 'Place' },
]

const load = async () => {
  loading.value = true
  work.value = await get('/api/work')
  work.value.sort((a, b) => a.order - b.order)
  loading.value = false
}

const openAdd = () => { editing.value = null; showForm.value = true }
const openEdit = (item: any) => { editing.value = item; showForm.value = true }
const openDelete = (item: any) => { deleting.value = item; showConfirm.value = true }

const save = async (data: any) => {
  // Send empty string resignation_date as null
  if (!data.resignation_date) data.resignation_date = null
  if (editing.value) {
    await put(`/api/work/${editing.value.id}`, data)
  } else {
    await post('/api/work', data)
  }
  showForm.value = false
  await load()
}

const confirmDelete = async () => {
  await del(`/api/work/${deleting.value.id}`)
  showConfirm.value = false
  await load()
}

onMounted(load)
</script>

<template>
  <div class="flex min-h-screen bg-gray-50 dark:bg-gray-900">
    <AdminSidebar />
    <div class="flex-1 flex flex-col">
      <AdminHeader title="Work Experience" />
      <main class="p-6">
        <div class="flex justify-between items-center mb-4">
          <p class="text-sm text-gray-500">Manage your work history.</p>
          <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="openAdd">
            + Add Work
          </button>
        </div>

        <DataTable :items="work" :columns :loading @edit="openEdit" @delete="openDelete" />

        <!-- Form modal -->
        <div v-if="showForm" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-lg">
            <h2 class="text-lg font-semibold mb-4">{{ editing ? 'Edit Work' : 'Add Work' }}</h2>
            <WorkForm :initial="editing" @submit="save" @cancel="showForm = false" />
          </div>
        </div>

        <ConfirmModal
          v-if="showConfirm"
          @confirm="confirmDelete"
          @cancel="showConfirm = false"
        />
      </main>
    </div>
  </div>
</template>

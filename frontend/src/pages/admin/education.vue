<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import DataTable from '@/components/admin/DataTable.vue'
import ConfirmModal from '@/components/admin/ConfirmModal.vue'
import EducationForm from '@/components/admin/forms/EducationForm.vue'
import { useAPI } from '@/composables/useAPI'

const { get, post, put, del } = useAPI()

const education = ref<any[]>([])
const loading = ref(false)
const showForm = ref(false)
const showConfirm = ref(false)
const editing = ref<any>(null)
const deleting = ref<any>(null)

const columns = [
  { key: 'course_name',      label: 'Course' },
  { key: 'join_date',        label: 'From' },
  { key: 'completion_date',  label: 'To' },
  { key: 'CGPA',             label: 'GPA' },
]

const load = async () => {
  loading.value = true
  const data = await get<any[]>('/api/education')
  education.value = data.sort((a, b) => a.order - b.order)
  loading.value = false
}

const openAdd = () => { editing.value = null; showForm.value = true }
const openEdit = (item: any) => { editing.value = item; showForm.value = true }
const openDelete = (item: any) => { deleting.value = item; showConfirm.value = true }

const save = async (data: any) => {
  // Send null for empty completion_date
  if (!data.completion_date) data.completion_date = null
  if (!data.CGPA) data.CGPA = null
  if (!data.CGPA_outof) data.CGPA_outof = null
  if (editing.value) {
    await put(`/api/education/${editing.value.id}`, data)
  } else {
    await post('/api/education', data)
  }
  showForm.value = false
  await load()
}

const confirmDelete = async () => {
  await del(`/api/education/${deleting.value.id}`)
  showConfirm.value = false
  await load()
}

onMounted(load)
</script>

<template>
  <div class="flex min-h-screen bg-gray-50 dark:bg-gray-900">
    <AdminSidebar />
    <div class="flex-1 flex flex-col">
      <AdminHeader title="Education" />
      <main class="p-6">
        <div class="flex justify-between items-center mb-4">
          <p class="text-sm text-gray-500">Manage your education history.</p>
          <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="openAdd">
            + Add Education
          </button>
        </div>

        <DataTable :items="education" :columns :loading @edit="openEdit" @delete="openDelete" />

        <div v-if="showForm" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-lg max-h-screen overflow-y-auto">
            <h2 class="text-lg font-semibold mb-4">{{ editing ? 'Edit Education' : 'Add Education' }}</h2>
            <EducationForm :initial="editing" @submit="save" @cancel="showForm = false" />
          </div>
        </div>

        <ConfirmModal v-if="showConfirm" @confirm="confirmDelete" @cancel="showConfirm = false" />
      </main>
    </div>
  </div>
</template>

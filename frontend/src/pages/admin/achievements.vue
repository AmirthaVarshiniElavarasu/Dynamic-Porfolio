<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import DataTable from '@/components/admin/DataTable.vue'
import ConfirmModal from '@/components/admin/ConfirmModal.vue'
import AchievementForm from '@/components/admin/forms/AchievementForm.vue'
import { useAPI } from '@/composables/useAPI'

const { get, post, put, del } = useAPI()

const achievements = ref<any[]>([])
const loading = ref(false)
const showForm = ref(false)
const showConfirm = ref(false)
const editing = ref<any>(null)
const deleting = ref<any>(null)

const columns = [{ key: 'description', label: 'Achievement' }]

const load = async () => {
  loading.value = true
  achievements.value = await get('/api/achievements')
  loading.value = false
}

const openAdd = () => { editing.value = null; showForm.value = true }
const openEdit = (item: any) => { editing.value = item; showForm.value = true }
const openDelete = (item: any) => { deleting.value = item; showConfirm.value = true }

const save = async (data: any) => {
  if (editing.value) {
    await put(`/api/achievements/${editing.value.id}`, data)
  } else {
    await post('/api/achievements', data)
  }
  showForm.value = false
  await load()
}

const confirmDelete = async () => {
  await del(`/api/achievements/${deleting.value.id}`)
  showConfirm.value = false
  await load()
}

onMounted(load)
</script>

<template>
  <div class="flex min-h-screen bg-gray-50 dark:bg-gray-900">
    <AdminSidebar />
    <div class="flex-1 flex flex-col">
      <AdminHeader title="Achievements" />
      <main class="p-6">
        <div class="flex justify-between items-center mb-4">
          <p class="text-sm text-gray-500">Manage your achievements and awards.</p>
          <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="openAdd">
            + Add Achievement
          </button>
        </div>

        <DataTable :items="achievements" :columns :loading @edit="openEdit" @delete="openDelete" />

        <div v-if="showForm" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-lg">
            <h2 class="text-lg font-semibold mb-4">{{ editing ? 'Edit Achievement' : 'Add Achievement' }}</h2>
            <AchievementForm :initial="editing" @submit="save" @cancel="showForm = false" />
          </div>
        </div>

        <ConfirmModal v-if="showConfirm" @confirm="confirmDelete" @cancel="showConfirm = false" />
      </main>
    </div>
  </div>
</template>

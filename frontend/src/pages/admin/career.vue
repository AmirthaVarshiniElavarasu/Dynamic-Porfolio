<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import ConfirmModal from '@/components/admin/ConfirmModal.vue'
import CareerObjectForm from '@/components/admin/forms/CareerObjectForm.vue'
import { useAPI } from '@/composables/useAPI'

const { get, post, put, del } = useAPI()

const items = ref<any[]>([])
const loading = ref(false)
const showForm = ref(false)
const showConfirm = ref(false)
const editing = ref<any>(null)
const deleting = ref<any>(null)

const load = async () => {
  loading.value = true
  items.value = await get('/api/career-object')
  loading.value = false
}

const openAdd = () => { editing.value = null; showForm.value = true }
const openEdit = (item: any) => { editing.value = item; showForm.value = true }
const openDelete = (item: any) => { deleting.value = item; showConfirm.value = true }

const save = async (data: any) => {
  if (editing.value) {
    await put(`/api/career-object/${editing.value.id}`, data)
  } else {
    await post('/api/career-object', data)
  }
  showForm.value = false
  await load()
}

const confirmDelete = async () => {
  await del(`/api/career-object/${deleting.value.id}`)
  showConfirm.value = false
  await load()
}

onMounted(load)
</script>

<template>
  <div class="flex min-h-screen bg-gray-50 dark:bg-gray-900">
    <AdminSidebar />
    <div class="flex-1 flex flex-col">
      <AdminHeader title="Hero / Career Object" />
      <main class="p-6">
        <div class="mb-2 p-3 bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-700 rounded-lg text-sm text-yellow-700 dark:text-yellow-300">
          ⚠ Only the first entry is shown on the hero section. Add one entry and edit it as needed.
        </div>

        <div class="flex justify-between items-center mb-4 mt-4">
          <p class="text-sm text-gray-500">Manage the hero headline and tagline.</p>
          <button
            class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50"
            :disabled="items.length > 0"
            @click="openAdd"
          >
            + Add Hero Text
          </button>
        </div>

        <div v-if="loading" class="text-center py-12 text-gray-400">Loading...</div>

        <div v-else class="space-y-4">
          <div
            v-for="item in items"
            :key="item.id"
            class="bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 p-5"
          >
            <h3 class="text-lg font-semibold mb-1">{{ item.title }}</h3>
            <p class="text-gray-500 text-sm whitespace-pre-line">{{ item.text }}</p>
            <div class="flex gap-2 mt-4">
              <button class="text-xs px-3 py-1 rounded border border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700" @click="openEdit(item)">Edit</button>
              <button class="text-xs px-3 py-1 rounded bg-red-50 text-red-600 border border-red-100 hover:bg-red-100 dark:bg-red-900/20 dark:text-red-400" @click="openDelete(item)">Delete</button>
            </div>
          </div>
          <p v-if="items.length === 0" class="text-center text-gray-400 italic py-12">No hero text yet. Add one.</p>
        </div>

        <div v-if="showForm" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-lg">
            <h2 class="text-lg font-semibold mb-4">{{ editing ? 'Edit Hero Text' : 'Add Hero Text' }}</h2>
            <CareerObjectForm :initial="editing" @submit="save" @cancel="showForm = false" />
          </div>
        </div>

        <ConfirmModal v-if="showConfirm" @confirm="confirmDelete" @cancel="showConfirm = false" />
      </main>
    </div>
  </div>
</template>

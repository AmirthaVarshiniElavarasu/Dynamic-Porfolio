<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import AboutForm from '@/components/admin/forms/AboutForm.vue'
import { useAPI } from '@/composables/useAPI'

const { get, post, put } = useAPI()

const item = ref<any>(null)
const loading = ref(false)
const showForm = ref(false)
const saving = ref(false)

const load = async () => {
  loading.value = true
  const data = await get<any[]>('/api/about-me')
  item.value = data[0] ?? null
  loading.value = false
}

const save = async (data: any) => {
  saving.value = true
  if (item.value) {
    await put(`/api/about-me/${item.value.id}`, data)
  } else {
    await post('/api/about-me', data)
  }
  saving.value = false
  showForm.value = false
  await load()
}

onMounted(load)
</script>

<template>
  <div class="flex min-h-screen bg-gray-50 dark:bg-gray-900">
    <AdminSidebar />
    <div class="flex-1 flex flex-col">
      <AdminHeader title="About Me" />
      <main class="p-6">
        <div class="mb-2 p-3 bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-700 rounded-lg text-sm text-yellow-700 dark:text-yellow-300">
          ⚠ Only the first entry is displayed. Edit the existing one rather than adding multiple.
        </div>

        <div v-if="loading" class="text-center py-12 text-gray-400">Loading...</div>

        <div v-else class="mt-4">
          <!-- Show current text -->
          <div v-if="item && !showForm" class="bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 p-6">
            <p class="text-gray-700 dark:text-gray-200 whitespace-pre-line leading-relaxed">
              {{ item.text }}
            </p>
            <button
              class="mt-4 px-4 py-2 text-sm border border-gray-200 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700"
              @click="showForm = true"
            >
              ✎ Edit
            </button>
          </div>

          <!-- No entry yet -->
          <div v-else-if="!item && !showForm" class="text-center py-12">
            <p class="text-gray-400 italic mb-4">No about me text yet.</p>
            <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="showForm = true">
              + Add About Me
            </button>
          </div>

          <!-- Inline form -->
          <div v-if="showForm" class="bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 p-6">
            <h2 class="text-lg font-semibold mb-4">{{ item ? 'Edit About Me' : 'Add About Me' }}</h2>
            <AboutForm :initial="item" @submit="save" @cancel="showForm = false" />
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

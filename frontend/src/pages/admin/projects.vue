<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import DataTable from '@/components/admin/DataTable.vue'
import ConfirmModal from '@/components/admin/ConfirmModal.vue'
import ProjectForm from '@/components/admin/forms/ProjectForm.vue'
import { useAPI } from '@/composables/useAPI'

const { get, post, put, del } = useAPI()

const projects = ref<any[]>([])
const descriptions = ref<any[]>([])
const loading = ref(false)
const showForm = ref(false)
const showConfirm = ref(false)
const showDescForm = ref(false)
const editing = ref<any>(null)
const deleting = ref<any>(null)
const selectedProject = ref<any>(null)  // for managing descriptions
const newDesc = ref('')

const columns = [
  { key: 'title',       label: 'Title' },
  { key: 'github_link', label: 'GitHub' },
  { key: 'hosted_link', label: 'Live Link' },
  { key: 'notes',       label: 'Notes' },
]

const load = async () => {
  loading.value = true
  const [p, d] = await Promise.all([
    get<any[]>('/api/projects'),
    get<any[]>('/api/project-descriptions'),
  ])
  projects.value = p
  descriptions.value = d
  loading.value = false
}

const descriptionsFor = (projectId: number) =>
  descriptions.value.filter(d => d.project_id === projectId)

const openAdd = () => { editing.value = null; showForm.value = true }
const openEdit = (item: any) => { editing.value = item; showForm.value = true }
const openDelete = (item: any) => { deleting.value = item; showConfirm.value = true }
const openDescriptions = (item: any) => { selectedProject.value = item; showDescForm.value = true }

const save = async (data: any) => {
  if (!data.hosted_link) data.hosted_link = null
  if (editing.value) {
    await put(`/api/projects/${editing.value.id}`, data)
  } else {
    await post('/api/projects', data)
  }
  showForm.value = false
  await load()
}

const confirmDelete = async () => {
  await del(`/api/projects/${deleting.value.id}`)
  showConfirm.value = false
  await load()
}

const addDescription = async () => {
  if (!newDesc.value.trim()) return
  await post('/api/project-descriptions', {
    text: newDesc.value,
    project_id: selectedProject.value.id,
  })
  newDesc.value = ''
  await load()
}

const deleteDescription = async (id: number) => {
  await del(`/api/project-descriptions/${id}`)
  await load()
}

onMounted(load)
</script>

<template>
  <div class="flex min-h-screen bg-gray-50 dark:bg-gray-900">
    <AdminSidebar />
    <div class="flex-1 flex flex-col">
      <AdminHeader title="Projects" />
      <main class="p-6">
        <div class="flex justify-between items-center mb-4">
          <p class="text-sm text-gray-500">Manage your projects.</p>
          <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="openAdd">
            + Add Project
          </button>
        </div>

        <!-- Projects table with extra Descriptions button -->
        <div class="overflow-x-auto rounded-xl border border-gray-200 dark:border-gray-700">
          <table class="w-full text-sm">
            <thead class="bg-gray-50 dark:bg-gray-800 text-gray-500">
              <tr>
                <th class="px-4 py-3 text-left">Title</th>
                <th class="px-4 py-3 text-left">GitHub</th>
                <th class="px-4 py-3 text-left">Live</th>
                <th class="px-4 py-3 text-left">Descriptions</th>
                <th class="px-4 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
              <tr v-if="loading">
                <td colspan="5" class="px-4 py-8 text-center text-gray-400">Loading...</td>
              </tr>
              <tr v-else-if="projects.length === 0">
                <td colspan="5" class="px-4 py-8 text-center text-gray-400 italic">No projects yet.</td>
              </tr>
              <tr
                v-for="p in projects" :key="p.id"
                class="bg-white dark:bg-gray-900 hover:bg-gray-50 dark:hover:bg-gray-800"
              >
                <td class="px-4 py-3 font-medium">{{ p.title }}</td>
                <td class="px-4 py-3 truncate max-w-[140px]">
                  <a :href="p.github_link" target="_blank" class="text-blue-500 hover:underline">Link</a>
                </td>
                <td class="px-4 py-3">
                  <a v-if="p.hosted_link" :href="p.hosted_link" target="_blank" class="text-blue-500 hover:underline">Link</a>
                  <span v-else class="text-gray-400">—</span>
                </td>
                <td class="px-4 py-3">
                  <button
                    class="text-xs px-2 py-1 rounded bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600"
                    @click="openDescriptions(p)"
                  >
                    {{ descriptionsFor(p.id).length }} bullet(s) ✎
                  </button>
                </td>
                <td class="px-4 py-3 text-right">
                  <div class="flex gap-2 justify-end">
                    <button class="text-xs px-3 py-1 rounded border border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700" @click="openEdit(p)">Edit</button>
                    <button class="text-xs px-3 py-1 rounded bg-red-50 text-red-600 border border-red-100 hover:bg-red-100 dark:bg-red-900/20 dark:text-red-400" @click="openDelete(p)">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Project form modal -->
        <div v-if="showForm" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-lg">
            <h2 class="text-lg font-semibold mb-4">{{ editing ? 'Edit Project' : 'Add Project' }}</h2>
            <ProjectForm :initial="editing" @submit="save" @cancel="showForm = false" />
          </div>
        </div>

        <!-- Descriptions manager modal -->
        <div v-if="showDescForm" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-lg">
            <h2 class="text-lg font-semibold mb-1">Descriptions</h2>
            <p class="text-sm text-gray-500 mb-4">{{ selectedProject?.title }}</p>

            <ul class="space-y-2 mb-4 max-h-48 overflow-y-auto">
              <li
                v-for="d in descriptionsFor(selectedProject?.id)"
                :key="d.id"
                class="flex items-start gap-2 text-sm"
              >
                <span class="text-blue-400 mt-1">▸</span>
                <span class="flex-1 text-gray-700 dark:text-gray-200">{{ d.text }}</span>
                <button class="text-red-400 hover:text-red-600 text-xs shrink-0" @click="deleteDescription(d.id)">✕</button>
              </li>
              <li v-if="descriptionsFor(selectedProject?.id).length === 0" class="text-gray-400 italic text-sm">
                No descriptions yet.
              </li>
            </ul>

            <div class="flex gap-2">
              <input
                v-model="newDesc"
                type="text"
                class="flex-1 border rounded-lg px-3 py-2 text-sm dark:bg-gray-700 dark:border-gray-600"
                placeholder="Add a bullet point..."
                @keyup.enter="addDescription"
              />
              <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="addDescription">Add</button>
            </div>

            <div class="flex justify-end mt-4">
              <button class="px-4 py-2 text-sm border border-gray-200 dark:border-gray-600 rounded-lg" @click="showDescForm = false">Done</button>
            </div>
          </div>
        </div>

        <ConfirmModal v-if="showConfirm" @confirm="confirmDelete" @cancel="showConfirm = false" />
      </main>
    </div>
  </div>
</template>

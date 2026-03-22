<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import ConfirmModal from '@/components/admin/ConfirmModal.vue'
import { useAPI } from '@/composables/useAPI'

const { get, post, put, del } = useAPI()

const categories = ref<any[]>([])
const skills = ref<any[]>([])
const loading = ref(false)

// Category form state
const showCatForm = ref(false)
const editingCat = ref<any>(null)
const catTitle = ref('')

// Skill form state
const showSkillForm = ref(false)
const editingSkill = ref<any>(null)
const skillName = ref('')
const skillCategoryId = ref(0)

// Delete state
const showConfirm = ref(false)
const deletingType = ref<'category' | 'skill'>('skill')
const deletingItem = ref<any>(null)

const load = async () => {
  loading.value = true
  const [c, s] = await Promise.all([
    get<any[]>('/api/skill-categories'),
    get<any[]>('/api/skills'),
  ])
  categories.value = c
  skills.value = s
  loading.value = false
}

const skillsFor = (catId: number) => skills.value.filter(s => s.category_id === catId)

// Category CRUD
const openAddCat = () => { editingCat.value = null; catTitle.value = ''; showCatForm.value = true }
const openEditCat = (c: any) => { editingCat.value = c; catTitle.value = c.title; showCatForm.value = true }
const saveCat = async () => {
  if (!catTitle.value.trim()) return
  if (editingCat.value) {
    await put(`/api/skill-categories/${editingCat.value.id}`, { title: catTitle.value })
  } else {
    await post('/api/skill-categories', { title: catTitle.value })
  }
  showCatForm.value = false
  await load()
}

// Skill CRUD
const openAddSkill = (catId: number) => {
  editingSkill.value = null
  skillName.value = ''
  skillCategoryId.value = catId
  showSkillForm.value = true
}
const openEditSkill = (s: any) => {
  editingSkill.value = s
  skillName.value = s.name
  skillCategoryId.value = s.category_id
  showSkillForm.value = true
}
const saveSkill = async () => {
  if (!skillName.value.trim()) return
  const data = { name: skillName.value, category_id: skillCategoryId.value }
  if (editingSkill.value) {
    await put(`/api/skills/${editingSkill.value.id}`, data)
  } else {
    await post('/api/skills', data)
  }
  showSkillForm.value = false
  await load()
}

// Delete
const openDelete = (type: 'category' | 'skill', item: any) => {
  deletingType.value = type
  deletingItem.value = item
  showConfirm.value = true
}
const confirmDelete = async () => {
  if (deletingType.value === 'category') {
    await del(`/api/skill-categories/${deletingItem.value.id}`)
  } else {
    await del(`/api/skills/${deletingItem.value.id}`)
  }
  showConfirm.value = false
  await load()
}

onMounted(load)
</script>

<template>
  <div class="flex min-h-screen bg-gray-50 dark:bg-gray-900">
    <AdminSidebar />
    <div class="flex-1 flex flex-col">
      <AdminHeader title="Skills" />
      <main class="p-6">
        <div class="flex justify-between items-center mb-6">
          <p class="text-sm text-gray-500">Manage skill categories and individual skills.</p>
          <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="openAddCat">
            + Add Category
          </button>
        </div>

        <div v-if="loading" class="text-center py-20 text-gray-400">Loading...</div>

        <div v-else class="space-y-6">
          <div
            v-for="cat in categories"
            :key="cat.id"
            class="bg-white dark:bg-gray-800 rounded-xl border border-gray-100 dark:border-gray-700 p-5"
          >
            <!-- Category header -->
            <div class="flex items-center justify-between mb-3">
              <h3 class="font-semibold text-gray-800 dark:text-gray-100">{{ cat.title }}</h3>
              <div class="flex gap-2">
                <button class="text-xs px-3 py-1 rounded border border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700" @click="openEditCat(cat)">Edit</button>
                <button class="text-xs px-3 py-1 rounded bg-red-50 text-red-600 border border-red-100 hover:bg-red-100 dark:bg-red-900/20 dark:text-red-400" @click="openDelete('category', cat)">Delete</button>
                <button class="text-xs px-3 py-1 rounded bg-blue-50 text-blue-600 border border-blue-100 hover:bg-blue-100 dark:bg-blue-900/20 dark:text-blue-400" @click="openAddSkill(cat.id)">+ Skill</button>
              </div>
            </div>

            <!-- Skills list -->
            <div class="flex flex-wrap gap-2">
              <div
                v-for="s in skillsFor(cat.id)"
                :key="s.id"
                class="flex items-center gap-1 px-3 py-1 bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 rounded-full text-sm"
              >
                <span>{{ s.name }}</span>
                <button class="ml-1 hover:text-blue-900 dark:hover:text-blue-100" title="Edit" @click="openEditSkill(s)">✎</button>
                <button class="ml-0.5 hover:text-red-500" title="Delete" @click="openDelete('skill', s)">✕</button>
              </div>
              <p v-if="skillsFor(cat.id).length === 0" class="text-sm text-gray-400 italic">No skills yet — click + Skill</p>
            </div>
          </div>

          <p v-if="categories.length === 0" class="text-center text-gray-400 italic py-12">
            No categories yet. Add one to get started.
          </p>
        </div>

        <!-- Category form modal -->
        <div v-if="showCatForm" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-sm">
            <h2 class="text-lg font-semibold mb-4">{{ editingCat ? 'Edit Category' : 'Add Category' }}</h2>
            <label class="block text-sm font-medium mb-1">Category Name</label>
            <input v-model="catTitle" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600 mb-4" placeholder="e.g. Frontend, Backend..." @keyup.enter="saveCat" />
            <div class="flex gap-3 justify-end">
              <button class="px-4 py-2 text-sm border border-gray-200 dark:border-gray-600 rounded-lg" @click="showCatForm = false">Cancel</button>
              <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="saveCat">Save</button>
            </div>
          </div>
        </div>

        <!-- Skill form modal -->
        <div v-if="showSkillForm" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-sm">
            <h2 class="text-lg font-semibold mb-4">{{ editingSkill ? 'Edit Skill' : 'Add Skill' }}</h2>
            <div class="space-y-3 mb-4">
              <div>
                <label class="block text-sm font-medium mb-1">Skill Name</label>
                <input v-model="skillName" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="e.g. Vue.js" @keyup.enter="saveSkill" />
              </div>
              <div>
                <label class="block text-sm font-medium mb-1">Category</label>
                <select v-model.number="skillCategoryId" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600">
                  <option :value="0" disabled>Select...</option>
                  <option v-for="c in categories" :key="c.id" :value="c.id">{{ c.title }}</option>
                </select>
              </div>
            </div>
            <div class="flex gap-3 justify-end">
              <button class="px-4 py-2 text-sm border border-gray-200 dark:border-gray-600 rounded-lg" @click="showSkillForm = false">Cancel</button>
              <button class="px-4 py-2 text-sm bg-blue-600 text-white rounded-lg hover:bg-blue-700" @click="saveSkill">Save</button>
            </div>
          </div>
        </div>

        <ConfirmModal
          v-if="showConfirm"
          :message="`Delete this ${deletingType}? ${deletingType === 'category' ? 'All skills in it will also be deleted.' : ''}`"
          @confirm="confirmDelete"
          @cancel="showConfirm = false"
        />
      </main>
    </div>
  </div>
</template>

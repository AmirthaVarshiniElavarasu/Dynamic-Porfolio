<script setup lang="ts">
import { ref, watch } from 'vue'

interface ProjectData {
  title: string
  github_link: string
  hosted_link: string
  notes: string
}

const props = defineProps<{ initial?: Partial<ProjectData> }>()
const emit = defineEmits<{ submit: [data: ProjectData]; cancel: [] }>()

const form = ref<ProjectData>({ title: '', github_link: '', hosted_link: '', notes: '' })
watch(() => props.initial, v => { if (v) Object.assign(form.value, v) }, { immediate: true })
</script>

<template>
  <div class="space-y-4">
    <div>
      <label class="block text-sm font-medium mb-1">Project Title *</label>
      <input v-model="form.title" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
    </div>
    <div>
      <label class="block text-sm font-medium mb-1">GitHub Link *</label>
      <input v-model="form.github_link" type="url" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="https://github.com/..." />
    </div>
    <div>
      <label class="block text-sm font-medium mb-1">Hosted / Live Link</label>
      <input v-model="form.hosted_link" type="url" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="https://..." />
    </div>
    <div>
      <label class="block text-sm font-medium mb-1">Notes</label>
      <textarea v-model="form.notes" rows="3" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
    </div>
    <div class="flex gap-3 justify-end pt-2">
      <button class="px-4 py-2 text-sm rounded-lg border border-gray-200 dark:border-gray-600" @click="emit('cancel')">Cancel</button>
      <button class="px-4 py-2 text-sm rounded-lg bg-blue-600 text-white hover:bg-blue-700" @click="emit('submit', form)">Save</button>
    </div>
  </div>
</template>

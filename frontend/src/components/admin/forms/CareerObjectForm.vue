<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{
  initial?: { title: string; text: string }
}>()
const emit = defineEmits<{ submit: [data: { title: string; text: string }]; cancel: [] }>()

const title = ref(props.initial?.title ?? '')
const text = ref(props.initial?.text ?? '')

watch(() => props.initial, (v) => {
  title.value = v?.title ?? ''
  text.value = v?.text ?? ''
})
</script>

<template>
  <div class="space-y-4">
    <div>
      <label class="block text-sm font-medium mb-1">Title / Headline</label>
      <input v-model="title" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="e.g. Full Stack Developer" />
    </div>
    <div>
      <label class="block text-sm font-medium mb-1">Tagline / Bio Text</label>
      <textarea v-model="text" rows="4" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="Short description shown on hero section..." />
    </div>
    <div class="flex gap-3 justify-end pt-2">
      <button class="px-4 py-2 text-sm rounded-lg border border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700" @click="emit('cancel')">Cancel</button>
      <button class="px-4 py-2 text-sm rounded-lg bg-blue-600 text-white hover:bg-blue-700" @click="emit('submit', { title, text })">Save</button>
    </div>
  </div>
</template>

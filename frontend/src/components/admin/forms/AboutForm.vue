<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{ initial?: { text: string } }>()
const emit = defineEmits<{ submit: [data: { text: string }]; cancel: [] }>()

const text = ref(props.initial?.text ?? '')
watch(() => props.initial, v => { text.value = v?.text ?? '' })
</script>

<template>
  <div class="space-y-4">
    <div>
      <label class="block text-sm font-medium mb-1">About Me Text</label>
      <textarea v-model="text" rows="6" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="Write about yourself..." />
    </div>
    <div class="flex gap-3 justify-end pt-2">
      <button class="px-4 py-2 text-sm rounded-lg border border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700" @click="emit('cancel')">Cancel</button>
      <button class="px-4 py-2 text-sm rounded-lg bg-blue-600 text-white hover:bg-blue-700" @click="emit('submit', { text })">Save</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{ initial?: { description: string } }>()
const emit = defineEmits<{ submit: [data: { description: string }]; cancel: [] }>()

const description = ref(props.initial?.description ?? '')
watch(() => props.initial, v => { description.value = v?.description ?? '' })
</script>

<template>
  <div class="space-y-4">
    <div>
      <label class="block text-sm font-medium mb-1">Achievement</label>
      <textarea v-model="description" rows="3" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="Describe your achievement..." />
    </div>
    <div class="flex gap-3 justify-end pt-2">
      <button class="px-4 py-2 text-sm rounded-lg border border-gray-200 dark:border-gray-600" @click="emit('cancel')">Cancel</button>
      <button class="px-4 py-2 text-sm rounded-lg bg-blue-600 text-white hover:bg-blue-700" @click="emit('submit', { description })">Save</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

interface WorkData {
  position: string
  company: string
  join_date: string
  resignation_date: string
  place: string
  order: number
}

const props = defineProps<{ initial?: Partial<WorkData> }>()
const emit = defineEmits<{ submit: [data: WorkData]; cancel: [] }>()

const form = ref<WorkData>({
  position: '',
  company: '',
  join_date: '',
  resignation_date: '',
  place: '',
  order: 0,
})

watch(() => props.initial, v => {
  if (v) Object.assign(form.value, v)
}, { immediate: true })
</script>

<template>
  <div class="space-y-4">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
      <div>
        <label class="block text-sm font-medium mb-1">Position *</label>
        <input v-model="form.position" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="e.g. Senior Developer" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">Company *</label>
        <input v-model="form.company" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="e.g. Acme Corp" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">Join Date * (YYYY-MM-DD)</label>
        <input v-model="form.join_date" type="date" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">Resignation Date (leave blank = Present)</label>
        <input v-model="form.resignation_date" type="date" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">Place *</label>
        <input v-model="form.place" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="e.g. Chennai, India" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">Display Order</label>
        <input v-model.number="form.order" type="number" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
      </div>
    </div>
    <div class="flex gap-3 justify-end pt-2">
      <button class="px-4 py-2 text-sm rounded-lg border border-gray-200 dark:border-gray-600" @click="emit('cancel')">Cancel</button>
      <button class="px-4 py-2 text-sm rounded-lg bg-blue-600 text-white hover:bg-blue-700" @click="emit('submit', form)">Save</button>
    </div>
  </div>
</template>

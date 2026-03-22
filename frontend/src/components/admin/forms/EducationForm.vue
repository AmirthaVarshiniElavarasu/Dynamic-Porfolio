<script setup lang="ts">
import { ref, watch } from 'vue'

interface EduData {
  course_name: string; join_date: string; completion_date: string
  course_work: string; CGPA: number | null; CGPA_outof: number | null; order: number
}

const props = defineProps<{ initial?: Partial<EduData> }>()
const emit = defineEmits<{ submit: [data: EduData]; cancel: [] }>()

const form = ref<EduData>({ course_name: '', join_date: '', completion_date: '', course_work: '', CGPA: null, CGPA_outof: null, order: 0 })
watch(() => props.initial, v => { if (v) Object.assign(form.value, v) }, { immediate: true })
</script>

<template>
  <div class="space-y-4">
    <div>
      <label class="block text-sm font-medium mb-1">Course / Degree Name</label>
      <input v-model="form.course_name" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="e.g. B.Tech Computer Science" />
    </div>
    <div class="grid grid-cols-2 gap-4">
      <div>
        <label class="block text-sm font-medium mb-1">Join Date *</label>
        <input v-model="form.join_date" type="date" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">Completion Date</label>
        <input v-model="form.completion_date" type="date" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
      </div>
    </div>
    <div>
      <label class="block text-sm font-medium mb-1">Coursework / Description</label>
      <textarea v-model="form.course_work" rows="3" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
    </div>
    <div class="grid grid-cols-3 gap-4">
      <div>
        <label class="block text-sm font-medium mb-1">CGPA</label>
        <input v-model.number="form.CGPA" type="number" step="0.01" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">Out of</label>
        <input v-model.number="form.CGPA_outof" type="number" step="0.01" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
      </div>
      <div>
        <label class="block text-sm font-medium mb-1">Order</label>
        <input v-model.number="form.order" type="number" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" />
      </div>
    </div>
    <div class="flex gap-3 justify-end pt-2">
      <button class="px-4 py-2 text-sm rounded-lg border border-gray-200 dark:border-gray-600" @click="emit('cancel')">Cancel</button>
      <button class="px-4 py-2 text-sm rounded-lg bg-blue-600 text-white hover:bg-blue-700" @click="emit('submit', form)">Save</button>
    </div>
  </div>
</template>

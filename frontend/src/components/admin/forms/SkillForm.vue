<script setup lang="ts">
import { ref, watch } from 'vue'

interface SkillData { name: string; category_id: number }

const props = defineProps<{
  initial?: Partial<SkillData>
  categories: { id: number; title: string }[]
}>()
const emit = defineEmits<{ submit: [data: SkillData]; cancel: [] }>()

const form = ref<SkillData>({ name: '', category_id: 0 })
watch(() => props.initial, v => { if (v) Object.assign(form.value, v) }, { immediate: true })
</script>

<template>
  <div class="space-y-4">
    <div>
      <label class="block text-sm font-medium mb-1">Skill Name *</label>
      <input v-model="form.name" type="text" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600" placeholder="e.g. Vue.js" />
    </div>
    <div>
      <label class="block text-sm font-medium mb-1">Category *</label>
      <select v-model.number="form.category_id" class="w-full border rounded-lg px-3 py-2 dark:bg-gray-700 dark:border-gray-600">
        <option value="0" disabled>Select category...</option>
        <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.title }}</option>
      </select>
    </div>
    <div class="flex gap-3 justify-end pt-2">
      <button class="px-4 py-2 text-sm rounded-lg border border-gray-200 dark:border-gray-600" @click="emit('cancel')">Cancel</button>
      <button class="px-4 py-2 text-sm rounded-lg bg-blue-600 text-white hover:bg-blue-700" @click="emit('submit', form)">Save</button>
    </div>
  </div>
</template>

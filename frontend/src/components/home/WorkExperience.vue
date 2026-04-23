<script setup lang="ts">
import type { WorkItem } from '@/composables/useWork'

defineProps<{ work: WorkItem[] }>()

// Format "2022-06-01" → "Jun 2022"
const fmt = (d: string) =>
  new Date(d).toLocaleDateString('en-US', { year: 'numeric', month: 'short' })
</script>

<template>
  <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow duration-300">
    <h2 class="text-2xl font-semibold mb-4 text-gray-900 dark:text-gray-100">Work Experience</h2>
    <div class="space-y-6">
      <div
        v-for="w in work"
        :key="w.id"
        class="border-l-4 border-blue-500 pl-4 pb-4 last:pb-0 hover:bg-gray-50 dark:hover:bg-gray-700 rounded-r-lg p-3 transition-colors duration-200"
      >
        <!-- Date range -->
        <span class="text-sm text-gray-500 dark:text-gray-400 font-medium">
          {{ fmt(w.join_date) }} – {{ w.resignation_date ? fmt(w.resignation_date) : 'Present' }}
        </span>

        <!-- Content -->
        <div class="mt-2">
          <p class="font-semibold text-lg text-gray-900 dark:text-gray-100">{{ w.position }}</p>
          <p class="text-sm text-gray-600 dark:text-gray-300">{{ w.company }} · {{ w.place }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

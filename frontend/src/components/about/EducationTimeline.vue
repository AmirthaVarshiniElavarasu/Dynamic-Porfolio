<script setup lang="ts">
import type { Education } from '@/composables/useEducation'

defineProps<{ education: Education[] }>()

const yr = (d: string) => new Date(d).getFullYear()
</script>

<template>
  <div class="space-y-8">
    <div
      v-for="e in education"
      :key="e.id"
      class="relative pl-12 pb-8 last:pb-0 hover:bg-gray-50 dark:hover:bg-gray-800/50 rounded-lg p-4 transition-colors duration-300"
    >
      <!-- dot on timeline -->
      <span class="absolute left-0 top-6 w-6 h-6 rounded-full bg-gradient-to-r from-blue-500 to-purple-500 border-4 border-white dark:border-gray-900 shadow-md" />

      <p class="text-sm text-gray-500 dark:text-gray-400 mb-2 font-medium">
        {{ yr(e.join_date) }} – {{ e.completion_date ? yr(e.completion_date) : 'Present' }}
      </p>

      <h3 class="font-bold text-xl text-gray-900 dark:text-gray-100 mb-2">
        {{ e.course_name }}
      </h3>

      <p v-if="e.course_work" class="text-gray-600 dark:text-gray-300 mb-2 leading-relaxed">
        {{ e.course_work }}
      </p>

      <p v-if="e.CGPA" class="text-sm text-gray-500 dark:text-gray-400">
        GPA: <span class="font-semibold text-blue-600 dark:text-blue-400">{{ e.CGPA }}</span> / {{ e.CGPA_outof }}
      </p>
    </div>

    <p v-if="education.length === 0" class="text-gray-400 italic text-center py-8">
      No education entries yet.
    </p>
  </div>
</template>

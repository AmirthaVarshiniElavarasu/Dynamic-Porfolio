<script setup lang="ts">
import type { Education } from '@/composables/useEducation'

defineProps<{ education: Education[] }>()

const yr = (d: string) => new Date(d).getFullYear()
</script>

<template>
  <div class="space-y-6">
    <div
      v-for="e in education"
      :key="e.id"
      class="relative pl-8 border-l-2 border-blue-200 dark:border-blue-800"
    >
      <!-- dot on timeline -->
      <span class="absolute -left-[9px] top-1 w-4 h-4 rounded-full bg-blue-500 border-2 border-white dark:border-gray-900" />

      <p class="text-sm text-gray-400 mb-1">
        {{ yr(e.join_date) }} –
        {{ e.completion_date ? yr(e.completion_date) : 'Present' }}
      </p>

      <h3 class="font-semibold text-gray-800 dark:text-gray-100">
        {{ e.course_name }}
      </h3>

      <p v-if="e.course_work" class="text-sm text-gray-500 dark:text-gray-400 mt-1">
        {{ e.course_work }}
      </p>

      <p v-if="e.CGPA" class="text-sm text-gray-500 dark:text-gray-400 mt-1">
        GPA: <span class="font-medium text-gray-700 dark:text-gray-200">{{ e.CGPA }}</span>
        / {{ e.CGPA_outof }}
      </p>
    </div>

    <p v-if="education.length === 0" class="text-gray-400 italic">
      No education entries yet.
    </p>
  </div>
</template>

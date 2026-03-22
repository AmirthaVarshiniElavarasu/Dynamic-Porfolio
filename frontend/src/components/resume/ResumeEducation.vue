<script setup lang="ts">
import type { Education } from '@/composables/useEducation'

defineProps<{ education: Education[] }>()

const yr = (d: string) => new Date(d).getFullYear()
</script>

<template>
  <section>
    <h2 class="text-2xl font-bold mb-6 pb-2 border-b border-gray-200 dark:border-gray-700">
      Education
    </h2>

    <div class="space-y-6">
      <div v-for="e in education" :key="e.id">
        <div class="flex flex-wrap items-baseline justify-between gap-2 mb-1">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100">
            {{ e.course_name }}
          </h3>
          <span class="text-sm text-gray-400">
            {{ yr(e.join_date) }} –
            {{ e.completion_date ? yr(e.completion_date) : 'Present' }}
          </span>
        </div>

        <p v-if="e.course_work" class="text-sm text-gray-500 dark:text-gray-400">
          {{ e.course_work }}
        </p>

        <p v-if="e.CGPA" class="text-sm text-gray-500 dark:text-gray-400 mt-1">
          GPA:
          <span class="font-medium text-gray-700 dark:text-gray-200">{{ e.CGPA }}</span>
          / {{ e.CGPA_outof }}
        </p>
      </div>

      <p v-if="education.length === 0" class="text-gray-400 italic">
        No education entries yet.
      </p>
    </div>
  </section>
</template>

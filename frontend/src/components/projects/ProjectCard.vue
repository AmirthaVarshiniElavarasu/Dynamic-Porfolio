<script setup lang="ts">
import type { Project } from '@/composables/useProjects'

defineProps<{ project: Project }>()
</script>

<template>
  <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm border border-gray-100 dark:border-gray-700 hover:shadow-md transition-shadow">
    <!-- Title + links -->
    <div class="flex items-start justify-between gap-4 mb-3">
      <h3 class="text-xl font-semibold text-gray-900 dark:text-gray-100">
        {{ project.title }}
      </h3>
      <div class="flex gap-2 shrink-0">
        <a
          :href="project.github_link"
          target="_blank"
          rel="noopener"
          class="text-sm px-3 py-1 rounded-lg border border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 transition"
        >
          GitHub
        </a>
        <a
          v-if="project.hosted_link"
          :href="project.hosted_link"
          target="_blank"
          rel="noopener"
          class="text-sm px-3 py-1 rounded-lg bg-blue-600 text-white hover:bg-blue-700 transition"
        >
          Live Demo
        </a>
      </div>
    </div>

    <!-- Description bullets -->
    <ul v-if="project.descriptions.length" class="space-y-1 mb-3">
      <li
        v-for="d in project.descriptions"
        :key="d.id"
        class="flex items-start gap-2 text-gray-600 dark:text-gray-300 text-sm"
      >
        <span class="text-blue-400 mt-1 shrink-0">▸</span>
        <span>{{ d.text }}</span>
      </li>
    </ul>

    <!-- Fallback to notes -->
    <p v-else-if="project.notes" class="text-gray-500 dark:text-gray-400 text-sm">
      {{ project.notes }}
    </p>
  </div>
</template>

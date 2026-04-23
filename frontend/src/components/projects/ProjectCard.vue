<script setup lang="ts">
import type { Project } from '@/composables/useProjects'

defineProps<{ project: Project }>()
</script>

<template>
  <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg border border-gray-100 dark:border-gray-700 hover:shadow-2xl hover:scale-105 transition-all duration-300 transform">
    <!-- Title + links -->
    <div class="flex items-start justify-between gap-4 mb-3">
      <h3 class="text-xl font-semibold text-gray-900 dark:text-gray-100 hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
        {{ project.title }}
      </h3>
      <div class="flex gap-2 shrink-0">
        <a
          :href="project.github_link"
          target="_blank"
          rel="noopener"
          class="text-sm px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 hover:bg-gray-100 dark:hover:bg-gray-700 hover:border-blue-500 transition-all duration-300 transform hover:scale-110"
        >
          GitHub
        </a>
        <a
          v-if="project.hosted_link"
          :href="project.hosted_link"
          target="_blank"
          rel="noopener"
          class="text-sm px-4 py-2 rounded-lg bg-gradient-to-r from-blue-500 to-purple-500 text-white hover:from-blue-600 hover:to-purple-600 transition-all duration-300 transform hover:scale-110 shadow-md"
        >
          Live Demo
        </a>
      </div>
    </div>

    <!-- Description bullets -->
    <ul v-if="project.descriptions.length" class="space-y-2 mb-3">
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

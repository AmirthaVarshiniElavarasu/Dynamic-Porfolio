<script setup lang="ts">
import { useTheme } from '@/composables/useTheme'

defineProps<{ title: string }>()

const { isDark, toggleTheme } = useTheme()
</script>

<template>
  <header class="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-6 py-4 flex items-center justify-between gap-4">
    <div>
      <h1 class="text-xl font-semibold text-gray-800 dark:text-gray-100">{{ title }}</h1>
      <p class="text-sm text-gray-500 dark:text-gray-400">Use the admin sidebar to edit your portfolio content.</p>
    </div>
    <div class="flex items-center gap-4">
      <button
        type="button"
        @click="toggleTheme"
        class="inline-flex items-center justify-center rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 text-gray-600 dark:text-gray-200 w-11 h-11 hover:bg-gray-100 dark:hover:bg-gray-800 transition"
        :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'"
      >
        <span v-if="isDark">☀️</span>
        <span v-else>🌙</span>
      </button>
      <div class="text-sm text-gray-500 dark:text-gray-400">Admin dashboard</div>
    </div>
  </header>
</template>

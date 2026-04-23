<script setup lang="ts">
import type { AboutMe } from '@/composables/useAbout'

defineProps<{ about: AboutMe }>()
</script>

<template>
  <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow duration-300">
    <h2 class="text-2xl font-semibold mb-4 text-gray-900 dark:text-gray-100">About Me</h2>
    <p class="text-gray-600 dark:text-gray-300 leading-relaxed whitespace-pre-line">
      {{ about.text }}
    </p>
  </div>
</template>

<script setup lang="ts">
import type { AboutMe } from '@/composables/useAbout'

defineProps<{ about: AboutMe }>()
</script>

<template>
  <div class="bg-gradient-to-br from-white to-gray-50 dark:from-gray-800 dark:to-gray-700 rounded-xl p-8 shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-100 dark:border-gray-600">
    <p class="text-gray-700 dark:text-gray-200 leading-relaxed whitespace-pre-line text-lg">
      {{ about.text }}
    </p>
  </div>
</template>

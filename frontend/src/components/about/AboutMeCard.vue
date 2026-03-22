<script setup lang="ts">
import type { AboutMe } from '@/composables/useAbout'

defineProps<{ about: AboutMe }>()
</script>

<template>
  <div class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm">
    <p class="text-gray-600 dark:text-gray-300 leading-relaxed whitespace-pre-line text-lg">
      {{ about.text }}
    </p>
  </div>
</template>

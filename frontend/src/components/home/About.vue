<script setup lang="ts">
import type { AboutMe } from '@/composables/useAbout'

defineProps<{ about: AboutMe }>()
</script>

<template>
  <div>
    <h2 class="text-2xl font-semibold mb-4">About Me</h2>
    <p class="text-gray-600 dark:text-gray-300 leading-relaxed whitespace-pre-line">
      {{ about.text }}
    </p>
  </div>
</template>

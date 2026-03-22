<script setup lang="ts">
import type { Achievement } from '@/composables/useAchievements'

defineProps<{ achievements: Achievement[] }>()
</script>

<template>
  <section v-if="achievements.length">
    <h2 class="text-2xl font-bold mb-6 pb-2 border-b border-gray-200 dark:border-gray-700">
      Achievements
    </h2>

    <ul class="space-y-2">
      <li
        v-for="a in achievements"
        :key="a.id"
        class="flex items-start gap-3 text-gray-600 dark:text-gray-300"
      >
        <span class="text-blue-500 mt-1 shrink-0">✦</span>
        <span>{{ a.description }}</span>
      </li>
    </ul>
  </section>
</template>

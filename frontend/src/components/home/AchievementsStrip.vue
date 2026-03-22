<script setup lang="ts">
import type { Achievement } from '@/composables/useAchievements'

defineProps<{ achievements: Achievement[] }>()
</script>

<template>
  <section v-if="achievements.length" class="bg-gray-50 dark:bg-gray-800 py-12 px-4">
    <div class="container mx-auto">
      <h2 class="text-2xl font-semibold mb-6 text-center">Achievements</h2>
      <ul class="space-y-3 max-w-2xl mx-auto">
        <li
          v-for="a in achievements"
          :key="a.id"
          class="flex items-start gap-3"
        >
          <span class="text-blue-500 mt-1">✦</span>
          <span class="text-gray-700 dark:text-gray-200">{{ a.description }}</span>
        </li>
      </ul>
    </div>
  </section>
</template>

<script setup lang="ts">
import type { Achievement } from '@/composables/useAchievements'

defineProps<{ achievements: Achievement[] }>()
</script>

<template>
  <section v-if="achievements.length" class="bg-gradient-to-r from-gray-50 to-blue-50 dark:from-gray-800 dark:to-gray-700 py-12 px-4">
    <div class="container mx-auto">
      <h2 class="text-2xl font-semibold mb-6 text-center text-gray-900 dark:text-gray-100">Achievements</h2>
      <ul class="space-y-4 max-w-2xl mx-auto">
        <li
          v-for="(a, index) in achievements"
          :key="a.id"
          class="flex items-start gap-3 bg-white dark:bg-gray-800 rounded-lg p-4 shadow-md hover:shadow-lg transform hover:scale-105 transition-all duration-300 animate-fade-in-up"
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <span class="text-blue-500 mt-1 text-xl">🏆</span>
          <span class="text-gray-700 dark:text-gray-200 leading-relaxed">{{ a.description }}</span>
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fade-in-up 0.6s ease-out forwards;
  opacity: 0;
}
</style>

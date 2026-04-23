<script setup lang="ts">
import type { SkillCategory } from '@/composables/useSkills'

defineProps<{ skillGroups: SkillCategory[] }>()
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
    <div
      v-for="group in skillGroups"
      :key="group.id"
      class="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-lg hover:shadow-xl hover:scale-105 transition-all duration-300 border border-gray-100 dark:border-gray-700"
    >
      <h3 class="font-semibold text-gray-800 dark:text-gray-100 mb-4 pb-2 border-b border-gray-200 dark:border-gray-600 text-lg">
        {{ group.title }}
      </h3>
      <div class="flex flex-wrap gap-3">
        <span
          v-for="skill in group.skills"
          :key="skill.id"
          class="px-4 py-2 text-sm bg-gradient-to-r from-blue-100 to-purple-100 dark:from-blue-900/50 dark:to-purple-900/50 text-blue-800 dark:text-blue-200 rounded-full hover:scale-110 transition-transform duration-200 cursor-default shadow-sm"
        >
          {{ skill.name }}
        </span>
      </div>
      <p v-if="group.skills.length === 0" class="text-sm text-gray-400 italic mt-2">
        No skills added yet
      </p>
    </div>
  </div>
</template>

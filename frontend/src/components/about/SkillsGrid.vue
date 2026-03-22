<script setup lang="ts">
import type { SkillCategory } from '@/composables/useSkills'

defineProps<{ skillGroups: SkillCategory[] }>()
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
    <div
      v-for="group in skillGroups"
      :key="group.id"
      class="bg-white dark:bg-gray-800 rounded-xl p-5 shadow-sm"
    >
      <h3 class="font-semibold text-gray-800 dark:text-gray-100 mb-3 pb-2 border-b border-gray-100 dark:border-gray-700">
        {{ group.title }}
      </h3>
      <div class="flex flex-wrap gap-2">
        <span
          v-for="skill in group.skills"
          :key="skill.id"
          class="px-3 py-1 text-sm bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 rounded-full"
        >
          {{ skill.name }}
        </span>
      </div>
      <p v-if="group.skills.length === 0" class="text-sm text-gray-400 italic">
        No skills added yet
      </p>
    </div>
  </div>
</template>

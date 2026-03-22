<script setup lang="ts">
import type { SkillCategory } from '@/composables/useSkills'

defineProps<{ skillGroups: SkillCategory[] }>()
</script>

<template>
  <section>
    <h2 class="text-2xl font-bold mb-6 pb-2 border-b border-gray-200 dark:border-gray-700">
      Skills
    </h2>

    <div class="space-y-4">
      <div v-for="group in skillGroups" :key="group.id" class="flex flex-wrap gap-x-6 gap-y-1">
        <span class="text-sm font-semibold text-gray-700 dark:text-gray-300 w-32 shrink-0">
          {{ group.title }}
        </span>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="skill in group.skills"
            :key="skill.id"
            class="px-2 py-0.5 text-sm bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 rounded"
          >
            {{ skill.name }}
          </span>
        </div>
      </div>

      <p v-if="skillGroups.length === 0" class="text-gray-400 italic">
        No skills added yet.
      </p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import ResumeWork from '@/components/resume/ResumeWork.vue'
import ResumeEducation from '@/components/resume/ResumeEducation.vue'
import ResumeSkills from '@/components/resume/ResumeSkills.vue'
import ResumeAchievements from '@/components/resume/ResumeAchievements.vue'
import { useWork } from '@/composables/useWork'
import { useEducation } from '@/composables/useEducation'
import { useSkills } from '@/composables/useSkills'
import { useAchievements } from '@/composables/useAchievements'

const { work, fetch: fetchWork } = useWork()
const { education, fetch: fetchEducation } = useEducation()
const { skillGroups, fetch: fetchSkills } = useSkills()
const { achievements, fetch: fetchAchievements } = useAchievements()

onMounted(async () => {
  await Promise.all([fetchWork(), fetchEducation(), fetchSkills(), fetchAchievements()])
})
</script>

<template>
  <main class="container mx-auto px-4 py-12 space-y-16">
    <h1 class="text-4xl font-bold">Resume</h1>
    <ResumeWork :work />
    <ResumeEducation :education />
    <ResumeSkills :skill-groups />
    <ResumeAchievements :achievements />
  </main>
</template>

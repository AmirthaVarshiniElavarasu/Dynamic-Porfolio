<script setup lang="ts">
import { onMounted } from 'vue'
import AboutMeCard from '@/components/about/AboutMeCard.vue'
import SkillsGrid from '@/components/about/SkillsGrid.vue'
import EducationTimeline from '@/components/about/EducationTimeline.vue'
import { useAbout } from '@/composables/useAbout'
import { useSkills } from '@/composables/useSkills'
import { useEducation } from '@/composables/useEducation'

const { about, fetch: fetchAbout } = useAbout()
const { skillGroups, fetch: fetchSkills } = useSkills()
const { education, fetch: fetchEducation } = useEducation()

onMounted(async () => {
  await Promise.all([fetchAbout(), fetchSkills(), fetchEducation()])
})
</script>

<template>
  <main class="container mx-auto px-4 py-12 space-y-16">
    <section>
      <h1 class="text-4xl font-bold mb-8">About Me</h1>
      <AboutMeCard :about />
    </section>

    <section>
      <h2 class="text-2xl font-semibold mb-6">Skills</h2>
      <SkillsGrid :skill-groups />
    </section>

    <section>
      <h2 class="text-2xl font-semibold mb-6">Education</h2>
      <EducationTimeline :education />
    </section>
  </main>
</template>

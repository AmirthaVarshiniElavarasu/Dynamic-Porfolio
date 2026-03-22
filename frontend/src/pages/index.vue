<script setup lang="ts">
import { onMounted } from 'vue'
import HeroSection from '@/components/home/HeroSection.vue'
import About from '@/components/home/About.vue'
import WorkExperience from '@/components/home/WorkExperience.vue'
import AchievementsStrip from '@/components/home/AchievementsStrip.vue'
import { useHero } from '@/composables/useHero'
import { useWork } from '@/composables/useWork'
import { useAchievements } from '@/composables/useAchievements'
import { useAbout } from '@/composables/useAbout'

const { hero, fetch: fetchHero } = useHero()
const { work, fetch: fetchWork } = useWork()
const { achievements, fetch: fetchAchievements } = useAchievements()
const { about, fetch: fetchAbout } = useAbout()

onMounted(async () => {
  await Promise.all([fetchHero(), fetchWork(), fetchAchievements(), fetchAbout()])
})
</script>

<template>
  <main>
    <HeroSection :hero />
    <div class="grid lg:grid-cols-2 gap-8 container mx-auto px-4 py-12">
      <About :about />
      <WorkExperience :work />
    </div>
    <AchievementsStrip :achievements />
  </main>
</template>

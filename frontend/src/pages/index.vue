<script setup lang="ts">
import { onMounted } from 'vue'
import HeroSection from '@/components/home/HeroSection.vue'
import About from '@/components/home/About.vue'
import WorkExperience from '@/components/home/WorkExperience.vue'
import AchievementsStrip from '@/components/home/AchievementsStrip.vue'
import ProjectCard from '@/components/projects/ProjectCard.vue'
import AboutMeCard from '@/components/about/AboutMeCard.vue'
import SkillsGrid from '@/components/about/SkillsGrid.vue'
import EducationTimeline from '@/components/about/EducationTimeline.vue'
import ResumeWork from '@/components/resume/ResumeWork.vue'
import ResumeEducation from '@/components/resume/ResumeEducation.vue'
import ResumeSkills from '@/components/resume/ResumeSkills.vue'
import ContactSection from '@/components/home/ContactSection.vue'
import { useHero } from '@/composables/useHero'
import { useWork } from '@/composables/useWork'
import { useAchievements } from '@/composables/useAchievements'
import { useAbout } from '@/composables/useAbout'
import { useProjects } from '@/composables/useProjects'
import { useSkills } from '@/composables/useSkills'
import { useEducation } from '@/composables/useEducation'

const { hero, fetch: fetchHero } = useHero()
const { work, fetch: fetchWork } = useWork()
const { achievements, fetch: fetchAchievements } = useAchievements()
const { about, fetch: fetchAbout } = useAbout()
const { projects, loading, fetch: fetchProjects } = useProjects()
const { skillGroups, fetch: fetchSkills } = useSkills()
const { education, fetch: fetchEducation } = useEducation()

onMounted(async () => {
  await Promise.all([
    fetchHero(),
    fetchWork(),
    fetchAchievements(),
    fetchAbout(),
    fetchProjects(),
    fetchSkills(),
    fetchEducation(),
  ])
})
</script>

<template>
  <main class="bg-gray-50 dark:bg-slate-950 text-gray-900 dark:text-gray-100">
    <HeroSection :hero />

    <section id="about" class="max-w-7xl mx-auto px-4 py-16 scroll-mt-24">
      <div class="grid lg:grid-cols-2 gap-8 items-start">
        <div>
          <h2 class="text-3xl font-bold mb-4">About Me</h2>
          <AboutMeCard :about="about" />
        </div>
        <div>
          <h2 class="text-3xl font-bold mb-4">Skills</h2>
          <SkillsGrid :skill-groups="skillGroups" />
        </div>
      </div>
    </section>

    <section id="work" class="max-w-7xl mx-auto px-4 py-16 scroll-mt-24">
      <div class="bg-white dark:bg-gray-900 rounded-3xl shadow-xl px-6 py-10">
        <h2 class="text-3xl font-bold mb-6">Experience</h2>
        <WorkExperience :work="work" />
      </div>
    </section>

    <section id="achievements" class="max-w-7xl mx-auto px-4 py-16 scroll-mt-24">
      <h2 class="text-3xl font-bold mb-6 text-center">Achievements</h2>
      <AchievementsStrip :achievements="achievements" />
    </section>

    <section id="projects" class="max-w-7xl mx-auto px-4 py-16 scroll-mt-24">
      <div class="flex items-center justify-between gap-4 mb-8 flex-col sm:flex-row">
        <div>
          <h2 class="text-3xl font-bold">Projects</h2>
          <p class="text-gray-600 dark:text-gray-300 mt-2 max-w-2xl">
            A collection of recent work, each showcasing the technologies and impact behind the project.
          </p>
        </div>
      </div>
      <div class="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        <ProjectCard
          v-for="project in projects"
          :key="project.id"
          :project="project"
        />
      </div>
      <div v-if="loading" class="text-center py-10 text-gray-500 dark:text-gray-400">Loading projects...</div>
    </section>

    <section id="resume" class="max-w-7xl mx-auto px-4 py-16 scroll-mt-24">
      <div class="bg-gradient-to-r from-blue-50 to-white dark:from-gray-900 dark:to-gray-800 rounded-3xl shadow-xl px-6 py-10">
        <h2 class="text-3xl font-bold mb-8">Resume</h2>
        <div class="grid gap-10 xl:grid-cols-2">
          <div class="space-y-10">
            <ResumeWork :work="work" />
            <ResumeEducation :education="education" />
          </div>
          <div class="space-y-10">
            <ResumeSkills :skill-groups="skillGroups" />
          </div>
        </div>
      </div>
    </section>

    <section id="contact" class="max-w-7xl mx-auto px-4 py-16 scroll-mt-24">
      <ContactSection />
    </section>
  </main>
</template>

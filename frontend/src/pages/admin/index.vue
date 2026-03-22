<script setup lang="ts">
import { ref, onMounted } from 'vue'
import AdminSidebar from '@/components/admin/AdminSidebar.vue'
import AdminHeader from '@/components/admin/AdminHeader.vue'
import { useAPI } from '@/composables/useAPI'

const { get } = useAPI()

const counts = ref({
  work: 0,
  projects: 0,
  skills: 0,
  education: 0,
  achievements: 0,
})

onMounted(async () => {
  const [work, projects, skills, edu, achievements] = await Promise.all([
    get<any[]>('/api/work'),
    get<any[]>('/api/projects'),
    get<any[]>('/api/skills'),
    get<any[]>('/api/education'),
    get<any[]>('/api/achievements'),
  ])
  counts.value = {
    work: work.length,
    projects: projects.length,
    skills: skills.length,
    education: edu.length,
    achievements: achievements.length,
  }
})

const cards = [
  { label: 'Work Entries',   key: 'work',         to: '/admin/work',         icon: '💼', color: 'bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300' },
  { label: 'Projects',       key: 'projects',     to: '/admin/projects',     icon: '📁', color: 'bg-purple-50 dark:bg-purple-900/20 text-purple-700 dark:text-purple-300' },
  { label: 'Skills',         key: 'skills',       to: '/admin/skills',       icon: '🛠',  color: 'bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-300' },
  { label: 'Education',      key: 'education',    to: '/admin/education',    icon: '🎓', color: 'bg-yellow-50 dark:bg-yellow-900/20 text-yellow-700 dark:text-yellow-300' },
  { label: 'Achievements',   key: 'achievements', to: '/admin/achievements', icon: '🏆', color: 'bg-orange-50 dark:bg-orange-900/20 text-orange-700 dark:text-orange-300' },
]
</script>

<template>
  <div class="flex min-h-screen bg-gray-50 dark:bg-gray-900">
    <AdminSidebar />
    <div class="flex-1 flex flex-col">
      <AdminHeader title="Dashboard" />
      <main class="p-6">

        <p class="text-gray-500 text-sm mb-6">Welcome back. Here's an overview of your portfolio content.</p>

        <!-- Stat cards -->
        <div class="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4 mb-8">
          <router-link
            v-for="card in cards"
            :key="card.key"
            :to="card.to"
            class="rounded-xl p-5 flex flex-col gap-2 hover:shadow-md transition-shadow cursor-pointer"
            :class="card.color"
          >
            <span class="text-2xl">{{ card.icon }}</span>
            <span class="text-3xl font-bold">{{ counts[card.key as keyof typeof counts] }}</span>
            <span class="text-sm font-medium">{{ card.label }}</span>
          </router-link>
        </div>

        <!-- Quick links -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <router-link
            to="/admin/career"
            class="rounded-xl border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 p-5 hover:shadow-md transition-shadow"
          >
            <p class="font-semibold mb-1">★ Hero / Career Object</p>
            <p class="text-sm text-gray-400">Update your headline and tagline shown on the homepage.</p>
          </router-link>
          <router-link
            to="/admin/about"
            class="rounded-xl border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 p-5 hover:shadow-md transition-shadow"
          >
            <p class="font-semibold mb-1">👤 About Me</p>
            <p class="text-sm text-gray-400">Edit your bio text shown on the About page.</p>
          </router-link>
        </div>

        <!-- View site link -->
        <div class="mt-8">
          <router-link
            to="/"
            class="inline-flex items-center gap-2 text-sm text-blue-600 hover:underline"
          >
            ↗ View live site
          </router-link>
        </div>

      </main>
    </div>
  </div>
</template>

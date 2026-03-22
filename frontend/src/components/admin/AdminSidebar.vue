<script setup lang="ts">
import { useAuth } from '@/composables/useAuth'
import { useRouter, useRoute } from 'vue-router'

const { logout } = useAuth()
const route = useRoute()

const links = [
  { to: '/admin',              label: 'Dashboard',   icon: '⊞' },
  { to: '/admin/career',       label: 'Hero / Career', icon: '★' },
  { to: '/admin/about',        label: 'About Me',    icon: '👤' },
  { to: '/admin/work',         label: 'Work',        icon: '💼' },
  { to: '/admin/projects',     label: 'Projects',    icon: '📁' },
  { to: '/admin/skills',       label: 'Skills',      icon: '🛠' },
  { to: '/admin/education',    label: 'Education',   icon: '🎓' },
  { to: '/admin/achievements', label: 'Achievements', icon: '🏆' },
]

const isActive = (path: string) =>
  path === '/admin' ? route.path === '/admin' : route.path.startsWith(path)
</script>

<template>
  <aside class="w-56 min-h-screen bg-gray-900 text-white flex flex-col">
    <div class="px-4 py-5 border-b border-gray-700">
      <p class="font-bold text-lg">Admin Panel</p>
    </div>

    <nav class="flex-1 py-4 space-y-1 px-2">
      <router-link
        v-for="link in links"
        :key="link.to"
        :to="link.to"
        class="flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition"
        :class="isActive(link.to)
          ? 'bg-blue-600 text-white'
          : 'text-gray-300 hover:bg-gray-800 hover:text-white'"
      >
        <span>{{ link.icon }}</span>
        <span>{{ link.label }}</span>
      </router-link>
    </nav>

    <div class="p-4 border-t border-gray-700">
      <button
        class="w-full text-sm text-gray-400 hover:text-white transition text-left"
        @click="logout"
      >
        ← Logout
      </button>
    </div>
  </aside>
</template>

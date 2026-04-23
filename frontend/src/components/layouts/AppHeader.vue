<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { useTheme } from '@/composables/useTheme'

const route = useRoute()
const mobileOpen = ref(false)
const activeHash = ref('#home')
const { isDark, toggleTheme } = useTheme()

const links = [
  { to: { path: '/', hash: '#home' }, label: 'Home', hash: '#home' },
  { to: { path: '/', hash: '#about' }, label: 'About', hash: '#about' },
  { to: { path: '/', hash: '#projects' }, label: 'Projects', hash: '#projects' },
  { to: { path: '/', hash: '#resume' }, label: 'Resume', hash: '#resume' },
  { to: { path: '/', hash: '#contact' }, label: 'Contact', hash: '#contact' },
]

const isActive = (link: { hash: string }) => activeHash.value === link.hash

const updateActiveSection = () => {
  if (route.path !== '/') return
  const sections = Array.from(document.querySelectorAll('section[id]')) as HTMLElement[]
  const offset = window.innerHeight / 3
  let current = '#home'

  sections.forEach((section) => {
    const top = section.getBoundingClientRect().top
    if (top <= offset) current = `#${section.id}`
  })

  activeHash.value = current
}

onMounted(() => {
  updateActiveSection()
  window.addEventListener('scroll', updateActiveSection, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', updateActiveSection)
})
</script>

<template>
  <header class="sticky top-0 z-30 bg-white/80 dark:bg-gray-950/80 backdrop-blur border-b border-gray-100 dark:border-gray-800">
    <div class="container mx-auto px-4 h-14 flex items-center justify-between">

      <!-- Logo -->
      <router-link to="/" class="font-bold text-lg tracking-tight">
        Portfolio
      </router-link>

      <!-- Desktop nav -->
      <nav class="hidden sm:flex items-center gap-1">
        <router-link
          v-for="link in links"
          :key="link.hash"
          :to="link.to"
          class="px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300 hover:bg-gradient-to-r hover:from-blue-500 hover:to-purple-500 hover:text-white transform hover:scale-105"
          :class="isActive(link)
            ? 'bg-gradient-to-r from-blue-500 to-purple-500 text-white shadow-lg'
            : 'text-gray-600 dark:text-gray-300'"
        >
          {{ link.label }}
        </router-link>
      </nav>

      <div class="hidden sm:flex items-center gap-2">
        <button
          type="button"
          @click="toggleTheme"
          class="inline-flex items-center justify-center rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-900 text-gray-600 dark:text-gray-200 w-11 h-11 hover:bg-gray-100 dark:hover:bg-gray-800 transition"
          :aria-label="isDark ? 'Switch to light mode' : 'Switch to dark mode'"
        >
          <span v-if="isDark">☀️</span>
          <span v-else>🌙</span>
        </button>
      </div>

      <!-- Mobile hamburger -->
      <button
        class="sm:hidden p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800"
        @click="mobileOpen = !mobileOpen"
      >
        <span class="block w-5 h-0.5 bg-current mb-1" />
        <span class="block w-5 h-0.5 bg-current mb-1" />
        <span class="block w-5 h-0.5 bg-current" />
      </button>
    </div>

    <!-- Mobile menu -->
    <div v-if="mobileOpen" class="sm:hidden border-t border-gray-100 dark:border-gray-800 px-4 py-3 space-y-2">
      <button
        type="button"
        @click="toggleTheme"
        class="flex w-full items-center justify-center gap-2 rounded-full border border-gray-200 dark:border-gray-700 px-4 py-2 text-sm text-gray-600 dark:text-gray-200 bg-white dark:bg-gray-900 hover:bg-gray-100 dark:hover:bg-gray-800 transition"
      >
        <span v-if="isDark">☀️</span>
        <span v-else>🌙</span>
        <span>{{ isDark ? 'Light mode' : 'Dark mode' }}</span>
      </button>
      <nav class="space-y-1">
        <router-link
          v-for="link in links"
          :key="link.hash"
          :to="link.to"
          class="block px-4 py-3 rounded-lg text-sm font-medium transition-all duration-300 hover:bg-gradient-to-r hover:from-blue-500 hover:to-purple-500 hover:text-white"
          :class="isActive(link)
            ? 'bg-gradient-to-r from-blue-500 to-purple-500 text-white shadow-lg'
            : 'text-gray-600 dark:text-gray-300'"
          @click="mobileOpen = false"
        >
          {{ link.label }}
        </router-link>
      </nav>
    </div>
  </header>
</template>

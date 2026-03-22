<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const mobileOpen = ref(false)

const links = [
  { to: '/',         label: 'Home' },
  { to: '/about',    label: 'About' },
  { to: '/projects', label: 'Projects' },
  { to: '/resume',   label: 'Resume' },
  { to: '/contact',  label: 'Contact' },
]

const isActive = (path: string) =>
  path === '/' ? route.path === '/' : route.path.startsWith(path)
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
          :key="link.to"
          :to="link.to"
          class="px-3 py-1.5 rounded-lg text-sm transition"
          :class="isActive(link.to)
            ? 'bg-gray-100 dark:bg-gray-800 font-medium'
            : 'text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100'"
        >
          {{ link.label }}
        </router-link>
      </nav>

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
    <div v-if="mobileOpen" class="sm:hidden border-t border-gray-100 dark:border-gray-800 px-4 py-3 space-y-1">
      <router-link
        v-for="link in links"
        :key="link.to"
        :to="link.to"
        class="block px-3 py-2 rounded-lg text-sm transition"
        :class="isActive(link.to)
          ? 'bg-gray-100 dark:bg-gray-800 font-medium'
          : 'text-gray-500 dark:text-gray-400'"
        @click="mobileOpen = false"
      >
        {{ link.label }}
      </router-link>
    </div>
  </header>
</template>

<script setup lang="ts">
import AppHeader from '@/components/layouts/AppHeader.vue'
import AppFooter from '@/components/layouts/AppFooter.vue'
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()

// Admin pages use their own layout (sidebar), no public header/footer
const isAdminPage = computed(() => route.path.startsWith('/admin'))
</script>

<template>
  <div class="min-h-screen flex flex-col bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100">
    <AppHeader v-if="!isAdminPage" />
    <div class="flex-1">
      <router-view />
    </div>
    <AppFooter v-if="!isAdminPage" />
  </div>
</template>

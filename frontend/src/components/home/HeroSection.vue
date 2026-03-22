<script setup lang="ts">
import type { Hero } from '@/composables/useHero'

defineProps<{ hero: Hero }>()
</script>

<template>
  <section class="text-center py-24 px-4">
    <h1 class="text-5xl font-bold mb-4">{{ hero.title }}</h1>
    <p class="text-xl text-gray-500 max-w-2xl mx-auto">{{ hero.text }}</p>
  </section>
</template>

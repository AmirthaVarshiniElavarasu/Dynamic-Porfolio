<script setup lang="ts">
defineProps<{ title: string }>()
</script>

<template>
  <header class="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 px-6 py-4">
    <h1 class="text-xl font-semibold text-gray-800 dark:text-gray-100">{{ title }}</h1>
  </header>
</template>

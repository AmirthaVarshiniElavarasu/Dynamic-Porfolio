<script setup lang="ts">
const year = new Date().getFullYear()
</script>

<template>
  <footer class="border-t border-gray-200 dark:border-gray-700 py-8 mt-16 bg-gray-50 dark:bg-gray-900">
    <div class="container mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4">
      <p class="text-sm text-gray-500 dark:text-gray-400">© {{ year }} Portfolio. All rights reserved.</p>
      <div class="flex gap-6">
        <a
          href="https://github.com"
          target="_blank"
          class="text-sm text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-300 transform hover:scale-110"
        >
          GitHub
        </a>
        <a
          href="https://linkedin.com"
          target="_blank"
          class="text-sm text-gray-500 dark:text-gray-400 hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-300 transform hover:scale-110"
        >
          LinkedIn
        </a>
      </div>
    </div>
  </footer>
</template>

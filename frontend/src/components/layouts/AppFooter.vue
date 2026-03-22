<script setup lang="ts">
const year = new Date().getFullYear()
</script>

<template>
  <footer class="border-t border-gray-100 dark:border-gray-800 py-8 mt-16">
    <div class="container mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4">
      <p class="text-sm text-gray-400">© {{ year }} Portfolio. All rights reserved.</p>
      <div class="flex gap-4">
        <a
          href="https://github.com"
          target="_blank"
          class="text-sm text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 transition"
        >
          GitHub
        </a>
        <a
          href="https://linkedin.com"
          target="_blank"
          class="text-sm text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 transition"
        >
          LinkedIn
        </a>
      </div>
    </div>
  </footer>
</template>

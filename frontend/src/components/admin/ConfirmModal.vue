<script setup lang="ts">
defineProps<{ message?: string }>()
const emit = defineEmits<{ confirm: []; cancel: [] }>()
</script>

<template>
  <div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
    <div class="bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 w-full max-w-sm">
      <p class="text-gray-800 dark:text-gray-100 mb-6">
        {{ message ?? 'Are you sure you want to delete this item?' }}
      </p>
      <div class="flex gap-3 justify-end">
        <button
          class="px-4 py-2 text-sm rounded-lg border border-gray-200 hover:bg-gray-50 dark:border-gray-600 dark:hover:bg-gray-700 transition"
          @click="emit('cancel')"
        >
          Cancel
        </button>
        <button
          class="px-4 py-2 text-sm rounded-lg bg-red-600 text-white hover:bg-red-700 transition"
          @click="emit('confirm')"
        >
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

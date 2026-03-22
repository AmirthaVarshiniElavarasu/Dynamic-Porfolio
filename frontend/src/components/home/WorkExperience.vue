<script setup lang="ts">
import type { WorkItem } from '@/composables/useWork'

defineProps<{ work: WorkItem[] }>()

// Format "2022-06-01" → "Jun 2022"
const fmt = (d: string) =>
  new Date(d).toLocaleDateString('en-US', { year: 'numeric', month: 'short' })
</script>

<template>
  <div>
    <h2 class="text-2xl font-semibold mb-4">Work Experience</h2>
    <div class="space-y-4">
      <div
        v-for="w in work"
        :key="w.id"
        class="flex gap-4 items-start"
      >
        <!-- Date range -->
        <span class="text-sm text-gray-400 whitespace-nowrap min-w-[130px]">
          {{ fmt(w.join_date) }} –
          {{ w.resignation_date ? fmt(w.resignation_date) : 'Present' }}
        </span>

        <!-- Divider -->
        <span class="text-gray-300 mt-0.5">|</span>

        <!-- Content -->
        <div>
          <p class="font-medium">{{ w.position }}</p>
          <p class="text-sm text-gray-500">{{ w.company }} · {{ w.place }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { WorkItem } from '@/composables/useWork'

defineProps<{ work: WorkItem[] }>()

const fmt = (d: string) =>
  new Date(d).toLocaleDateString('en-US', { year: 'numeric', month: 'short' })
</script>

<template>
  <section>
    <h2 class="text-2xl font-bold mb-6 pb-2 border-b border-gray-200 dark:border-gray-700">
      Work Experience
    </h2>

    <div class="space-y-8">
      <div v-for="w in work" :key="w.id">
        <!-- Header row -->
        <div class="flex flex-wrap items-baseline justify-between gap-2 mb-2">
          <div>
            <h3 class="text-lg font-semibold text-gray-900 dark:text-gray-100">
              {{ w.position }}
            </h3>
            <p class="text-gray-500 dark:text-gray-400">
              {{ w.company }} · {{ w.place }}
            </p>
          </div>
          <span class="text-sm text-gray-400 whitespace-nowrap">
            {{ fmt(w.join_date) }} –
            {{ w.resignation_date ? fmt(w.resignation_date) : 'Present' }}
          </span>
        </div>

        <!-- Description bullets -->
        <ul v-if="w.descriptions.length" class="space-y-1 mt-2">
          <li
            v-for="d in w.descriptions"
            :key="d.id"
            class="flex items-start gap-2 text-sm text-gray-600 dark:text-gray-300"
          >
            <span class="text-blue-400 mt-1 shrink-0">▸</span>
            <span>{{ d.text }}</span>
          </li>
        </ul>
      </div>

      <p v-if="work.length === 0" class="text-gray-400 italic">
        No work entries yet.
      </p>
    </div>
  </section>
</template>

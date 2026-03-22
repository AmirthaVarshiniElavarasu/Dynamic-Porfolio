<script setup lang="ts" generic="T extends { id: number }">
defineProps<{
  items: T[]
  columns: { key: keyof T; label: string }[]
  loading?: boolean
}>()

const emit = defineEmits<{
  edit: [item: T]
  delete: [item: T]
}>()
</script>

<template>
  <div class="overflow-x-auto rounded-xl border border-gray-200 dark:border-gray-700">
    <table class="w-full text-sm">
      <thead class="bg-gray-50 dark:bg-gray-800 text-gray-500 dark:text-gray-400">
        <tr>
          <th
            v-for="col in columns"
            :key="String(col.key)"
            class="px-4 py-3 text-left font-medium"
          >
            {{ col.label }}
          </th>
          <th class="px-4 py-3 text-right">Actions</th>
        </tr>
      </thead>

      <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
        <tr v-if="loading">
          <td :colspan="columns.length + 1" class="px-4 py-8 text-center text-gray-400">
            Loading...
          </td>
        </tr>
        <tr v-else-if="items.length === 0">
          <td :colspan="columns.length + 1" class="px-4 py-8 text-center text-gray-400 italic">
            No entries yet.
          </td>
        </tr>
        <tr
          v-for="item in items"
          :key="item.id"
          class="bg-white dark:bg-gray-900 hover:bg-gray-50 dark:hover:bg-gray-800 transition"
        >
          <td
            v-for="col in columns"
            :key="String(col.key)"
            class="px-4 py-3 text-gray-700 dark:text-gray-200 max-w-xs truncate"
          >
            {{ item[col.key] }}
          </td>
          <td class="px-4 py-3 text-right">
            <div class="flex gap-2 justify-end">
              <button
                class="text-xs px-3 py-1 rounded border border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 transition"
                @click="emit('edit', item)"
              >
                Edit
              </button>
              <button
                class="text-xs px-3 py-1 rounded bg-red-50 text-red-600 border border-red-100 hover:bg-red-100 dark:bg-red-900/20 dark:border-red-800 dark:text-red-400 transition"
                @click="emit('delete', item)"
              >
                Delete
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

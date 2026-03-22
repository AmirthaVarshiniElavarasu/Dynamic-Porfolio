<script setup lang="ts">
import { onMounted } from 'vue'
import ProjectCard from '@/components/projects/ProjectCard.vue'
import { useProjects } from '@/composables/useProjects'

const { projects, loading, fetch } = useProjects()

onMounted(fetch)
</script>

<template>
  <main class="container mx-auto px-4 py-12">
    <h1 class="text-4xl font-bold mb-8">Projects</h1>

    <div v-if="loading" class="text-center py-20 text-gray-400">Loading...</div>

    <div v-else class="space-y-8">
      <ProjectCard
        v-for="project in projects"
        :key="project.id"
        :project
      />
    </div>
  </main>
</template>

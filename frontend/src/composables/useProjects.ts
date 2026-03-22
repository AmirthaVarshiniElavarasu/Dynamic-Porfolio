import { ref } from 'vue'
import { useAPI } from './useAPI'

export interface Project {
  id: number
  title: string
  github_link: string
  hosted_link: string | null
  notes: string | null
  descriptions: ProjectDescription[]
}

export interface ProjectDescription {
  id: number
  text: string
  project_id: number
}

export const useProjects = () => {
  const { get } = useAPI()
  const projects = ref<Project[]>([])
  const loading = ref(false)
  const error = ref('')

  const fetch = async () => {
    loading.value = true
    try {
      const [projectData, descData] = await Promise.all([
        get<Omit<Project, 'descriptions'>[]>('/api/projects'),
        get<ProjectDescription[]>('/api/project-descriptions'),
      ])

      // Join descriptions into their project by project_id
      projects.value = projectData.map(p => ({
        ...p,
        descriptions: descData.filter(d => d.project_id === p.id),
      }))
    } catch (e: any) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { projects, loading, error, fetch }
}

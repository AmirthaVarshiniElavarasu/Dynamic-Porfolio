import { ref } from 'vue'
import { useAPI } from './useAPI'

export interface Education {
  id: number
  course_name: string
  join_date: string          // ISO string
  completion_date: string | null
  course_work: string
  CGPA: number | null
  CGPA_outof: number | null
  order: number
}

export const useEducation = () => {
  const { get } = useAPI()
  const education = ref<Education[]>([])
  const loading = ref(false)
  const error = ref('')

  const fetch = async () => {
    loading.value = true
    try {
      const data = await get<Education[]>('/api/education')
      education.value = data.sort((a, b) => a.order - b.order)
    } catch (e: any) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { education, loading, error, fetch }
}

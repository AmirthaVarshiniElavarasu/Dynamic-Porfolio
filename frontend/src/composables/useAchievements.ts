import { ref } from 'vue'
import { useAPI } from './useAPI'

export interface Achievement {
  id: number
  description: string
}

export const useAchievements = () => {
  const { get } = useAPI()
  const achievements = ref<Achievement[]>([])
  const loading = ref(false)
  const error = ref('')

  const fetch = async () => {
    loading.value = true
    try {
      achievements.value = await get<Achievement[]>('/api/achievements')
    } catch (e: any) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { achievements, loading, error, fetch }
}

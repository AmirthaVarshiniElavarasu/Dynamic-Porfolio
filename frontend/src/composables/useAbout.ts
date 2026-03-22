import { ref } from 'vue'
import { useAPI } from './useAPI'

export interface AboutMe {
  id: number
  text: string
}

export const useAbout = () => {
  const { get } = useAPI()
  const about = ref<AboutMe>({ id: 0, text: '' })
  const loading = ref(false)
  const error = ref('')

  const fetch = async () => {
    loading.value = true
    try {
      const data = await get<AboutMe[]>('/api/about-me')
      about.value = data[0] ?? { id: 0, text: '' }
    } catch (e: any) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { about, loading, error, fetch }
}

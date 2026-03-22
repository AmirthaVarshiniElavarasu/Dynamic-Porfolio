import { ref } from 'vue'
import { useAPI } from './useAPI'

export interface Hero {
  id: number
  title: string
  text: string
}

export const useHero = () => {
  const { get } = useAPI()
  const hero = ref<Hero>({ id: 0, title: '', text: '' })
  const loading = ref(false)
  const error = ref('')

  const fetch = async () => {
    loading.value = true
    try {
      // career-object returns an array — we only need the first item
      const data = await get<Hero[]>('/api/career-object')
      hero.value = data[0] ?? { id: 0, title: '', text: '' }
    } catch (e: any) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { hero, loading, error, fetch }
}

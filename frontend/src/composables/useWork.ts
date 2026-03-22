import { ref } from 'vue'
import { useAPI } from './useAPI'

export interface WorkItem {
  id: number
  position: string
  company: string
  join_date: string        // ISO string e.g. "2022-06-01"
  resignation_date: string | null
  place: string
  order: number
  descriptions: WorkDescription[]
}

export interface WorkDescription {
  id: number
  text: string
  work_id: number
}

export const useWork = () => {
  const { get } = useAPI()
  const work = ref<WorkItem[]>([])
  const loading = ref(false)
  const error = ref('')

  const fetch = async () => {
    loading.value = true
    try {
      // Fetch both in parallel — descriptions are separate endpoint
      const [workData, descData] = await Promise.all([
        get<Omit<WorkItem, 'descriptions'>[]>('/api/work'),
        get<WorkDescription[]>('/api/work-descriptions'),
      ])

      // Join descriptions into their work entry by work_id
      work.value = workData
        .sort((a, b) => a.order - b.order)
        .map(w => ({
          ...w,
          descriptions: descData.filter(d => d.work_id === w.id),
        }))
    } catch (e: any) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { work, loading, error, fetch }
}

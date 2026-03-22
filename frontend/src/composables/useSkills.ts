import { ref } from 'vue'
import { useAPI } from './useAPI'

export interface SkillCategory {
  id: number
  title: string
  skills: Skill[]
}

export interface Skill {
  id: number
  name: string
  category_id: number
}

export const useSkills = () => {
  const { get } = useAPI()
  const skillGroups = ref<SkillCategory[]>([])
  const loading = ref(false)
  const error = ref('')

  const fetch = async () => {
    loading.value = true
    try {
      const [categories, skills] = await Promise.all([
        get<Omit<SkillCategory, 'skills'>[]>('/api/skill-categories'),
        get<Skill[]>('/api/skills'),
      ])

      // Nest each skill under its category
      skillGroups.value = categories.map(cat => ({
        ...cat,
        skills: skills.filter(s => s.category_id === cat.id),
      }))
    } catch (e: any) {
      error.value = e.message
    } finally {
      loading.value = false
    }
  }

  return { skillGroups, loading, error, fetch }
}

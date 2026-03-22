import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAPI } from './useAPI'

// Global auth state — shared across all components
const isLoggedIn = ref(false)
const isChecked = ref(false)  // has auth been verified this session?

export const useAuth = () => {
  const router = useRouter()
  const { post, get } = useAPI()

  const login = async (email: string, password: string) => {
    await post('/api/AdminLogin', { email, password })
    isLoggedIn.value = true
    router.push('/admin')
  }

  const logout = async () => {
    await post('/api/Logout', {})
    isLoggedIn.value = false
    router.push('/admin/login')
  }

  // Check if session is still valid (call on page refresh)
  const checkAuth = async (): Promise<boolean> => {
    if (isChecked.value) return isLoggedIn.value
    try {
      await get('/api/auth/check')
      isLoggedIn.value = true
    } catch {
      isLoggedIn.value = false
    }
    isChecked.value = true
    return isLoggedIn.value
  }

  return { login, logout, checkAuth, isLoggedIn }
}

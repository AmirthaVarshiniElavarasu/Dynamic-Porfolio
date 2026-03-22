import { useAuth } from '@/composables/useAuth'

export const authGuard = async () => {
  const { checkAuth, isLoggedIn } = useAuth()
  await checkAuth()
  return isLoggedIn.value
}
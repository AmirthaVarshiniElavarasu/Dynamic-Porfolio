import { useAuth } from '@/composables/useAuth'

export const guestGuard = async () => {
  const { checkAuth, isLoggedIn } = useAuth()
  await checkAuth()
  return !isLoggedIn.value
}

import { ref } from 'vue'
import { useRouter } from 'vue-router'


// Global auth state — shared across all components
const isLoggedIn = ref(false)
const isChecked = ref(false) 

const getToken =() => localStorage.getItem("admin_token");
const setToken =(t: string) => localStorage.setItem("admin_token",t);
const clearToken =() => localStorage.removeItem("admin_token");

export const useAuth = () => {
  const router = useRouter()
  const API_BASE = import.meta.env.VITE_API_BASE || 'http://localStorage:5000'

  const login = async (email: string, password: string) => {
    const res = await fetch(`${API_BASE}/api/AdminLogin`,{
      method:'POST',
      headers:{ 'Content-Type':'application/json'},
      body: JSON.stringify({email,password}),
    })
    const data = await res.json()
    if (!res.ok) throw {status:res.status,data}

    setToken(data.token)
    isLoggedIn.value = true
    router.push('/admin')
  }

  const logout = async () => {
    clearToken()
    isLoggedIn.value = false
    router.push('/admin/login')
  }

  // Check if session is still valid (call on page refresh)
  const checkAuth = async (): Promise<boolean> => {
    if (isChecked.value) return isLoggedIn.value
    const token = getToken()
    if (!token){
    isLoggedIn.value=false
    isChecked.value = true
    return false
  }
  try{
    const res=await fetch(`${API_BASE}/api/auth/check`,{
      headers:{Authorization: `Bearer ${token}`},
    })
    isLoggedIn.value=res.ok
  }catch{
    isLoggedIn.value = false
  }
  isChecked.value = true
  return isLoggedIn.value
  }
  return { login, logout, checkAuth, isLoggedIn, getToken }
}

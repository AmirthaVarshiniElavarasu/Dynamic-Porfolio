// Base API wrapper — always sends session cookie
const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000'

const getToken = () => localStorage.getItem('admin_token')

const authHeaders = () => {
  const token = getToken()
  return token
    ? {'Content-Type': 'application/json', Authorization:`Bearer ${token}`}
    : {'Content-Type': 'application/json'}}
export const useAPI = () => {

  const get = async <T>(path: string): Promise<T> => {
    const res = await fetch(`${API_BASE}${path}`, {
      headers: authHeaders(),       
    })
    if (!res.ok) throw new Error(`GET ${path} failed: ${res.status}`)
    return res.json()
  }

  const post = async <T>(path: string, body: object): Promise<T> => {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'POST',
      
      headers: authHeaders(),
      body: JSON.stringify(body),
    })
    if (!res.ok) {
      const err = await res.json().catch(() => ({ message: 'Request failed' }))
      throw { status: res.status, data: err }
    }
    return res.json()
  }

  const put = async <T>(path: string, body: object): Promise<T> => {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'PUT',
      
      headers: authHeaders(),
      body: JSON.stringify(body),
    })
    if (!res.ok) {
      const err = await res.json().catch(() => ({ message: 'Request failed' }))
      throw { status: res.status, data: err }
    }
    return res.json()
  }

  const del = async <T>(path: string): Promise<T> => {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'DELETE',
      headers: authHeaders(),
    })
    if (!res.ok) throw new Error(`DELETE ${path} failed: ${res.status}`)
    return res.json()
  }

  return { get, post, put, del }
}

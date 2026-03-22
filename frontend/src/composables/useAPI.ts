// Base API wrapper — always sends session cookie
const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:5000'

export const useAPI = () => {

  const get = async <T>(path: string): Promise<T> => {
    const res = await fetch(`${API_BASE}${path}`, {
      credentials: 'include',   // ← sends Flask session cookie
    })
    if (!res.ok) throw new Error(`GET ${path} failed: ${res.status}`)
    return res.json()
  }

  const post = async <T>(path: string, body: object): Promise<T> => {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'POST',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
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
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
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
      credentials: 'include',
    })
    if (!res.ok) throw new Error(`DELETE ${path} failed: ${res.status}`)
    return res.json()
  }

  return { get, post, put, del }
}

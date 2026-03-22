<script setup lang="ts">
import { ref } from 'vue'
import { useAuth } from '@/composables/useAuth'

const { login } = useAuth()
const email = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

const submit = async () => {
  loading.value = true
  error.value = ''
  try {
    await login(email.value, password.value)
  } catch (e: any) {
    error.value = e?.data?.message ?? 'Invalid credentials'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
    <div class="w-full max-w-sm bg-white dark:bg-gray-800 rounded-xl shadow-lg p-8">
      <h1 class="text-2xl font-bold mb-6 text-center">Admin Login</h1>

      <div class="space-y-4">
        <div>
          <label class="block text-sm font-medium mb-1">Email</label>
          <input
            v-model="email"
            type="email"
            class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="admin@example.com"
            @keyup.enter="submit"
          />
        </div>

        <div>
          <label class="block text-sm font-medium mb-1">Password</label>
          <input
            v-model="password"
            type="password"
            class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="••••••••"
            @keyup.enter="submit"
          />
        </div>

        <p v-if="error" class="text-sm text-red-500 bg-red-50 rounded px-3 py-2">
          {{ error }}
        </p>

        <button
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 rounded-lg transition disabled:opacity-60"
          :disabled="loading"
          @click="submit"
        >
          {{ loading ? 'Signing in...' : 'Sign In' }}
        </button>
      </div>
    </div>
  </div>
</template>

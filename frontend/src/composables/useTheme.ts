import { ref, computed } from 'vue'

const theme = ref('light')

const isDark = computed(() => theme.value === 'dark')

const setTheme = (value: string) => {
  theme.value = value

  if (value === 'dark') {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }

  localStorage.setItem('theme', value)
}

const toggleTheme = () => setTheme(isDark.value ? 'light' : 'dark')

// Initialize theme from DOM class
const initTheme = () => {
  const hasDarkClass = document.documentElement.classList.contains('dark')
  theme.value = hasDarkClass ? 'dark' : 'light'
}

initTheme()

export const useTheme = () => ({
  theme: computed(() => theme.value),
  isDark,
  setTheme,
  toggleTheme,
})
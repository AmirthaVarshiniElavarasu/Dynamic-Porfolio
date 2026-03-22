import { createRouter, createWebHistory } from 'vue-router'
import { useAuth } from '@/composables/useAuth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // ── Public pages ──────────────────────────────────────
    {
      path: '/',
      component: () => import('@/pages/index.vue'),
    },
    {
      path: '/about',
      component: () => import('@/pages/about.vue'),
    },
    {
      path: '/projects',
      component: () => import('@/pages/Projects.vue'),
    },
    {
      path: '/resume',
      component: () => import('@/pages/resume.vue'),
    },
    {
      path: '/contact',
      component: () => import('@/pages/contact.vue'),
    },

    // ── Admin pages ────────────────────────────────────────
    {
      path: '/admin/login',
      component: () => import('@/pages/admin/login.vue'),
      meta: { guestOnly: true },  // redirect to /admin if already logged in
    },
    {
      path: '/admin',
      component: () => import('@/pages/admin/index.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/admin/work',
      component: () => import('@/pages/admin/work.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/admin/projects',
      component: () => import('@/pages/admin/projects.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/admin/skills',
      component: () => import('@/pages/admin/skills.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/admin/education',
      component: () => import('@/pages/admin/education.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/admin/about',
      component: () => import('@/pages/admin/about.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/admin/achievements',
      component: () => import('@/pages/admin/achievements.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/admin/career',
      component: () => import('@/pages/admin/career.vue'),
      meta: { requiresAuth: true },
    },
  ],
})

// ── Route guard ────────────────────────────────────────────
router.beforeEach(async (to) => {
  const { checkAuth, isLoggedIn } = useAuth()

  if (to.meta.requiresAuth || to.meta.guestOnly) {
    await checkAuth()
  }

  if (to.meta.requiresAuth && !isLoggedIn.value) {
    return '/admin/login'
  }

  if (to.meta.guestOnly && isLoggedIn.value) {
    return '/admin'
  }
})

export default router

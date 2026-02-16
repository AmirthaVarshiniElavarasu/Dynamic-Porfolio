import { createRouter, createWebHistory } from 'vue-router';


const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to,from,next)=>{
    const token =localStorage.getItem('token');

    if (to.meta.requiresAuth){
        if(!token){
            return next('/login');
        }
    }
    next();
})

export default router;
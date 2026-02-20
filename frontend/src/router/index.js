import { createRouter, createWebHistory } from 'vue-router';
import Adminlogin from '../components/AdminLogin.vue';

const routes = [
    {path: '/adminlogin', name:'AdminLogin', component: Adminlogin,meta:{requiresAuth:true}}
]
const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to,from,next)=>{
    const token =localStorage.getItem('token');

    if (to.meta.requiresAuth){
        if(!token){
            return next('/adminlogin');
        }
    }
    next();
})

export default router;
<template>
    <div class="login">
        <h2>Admin Login</h2>
        <form @submit.prevent="handleLogin">
            <input type="email" v-model="email">
        </form>

    </div>
</template>

<script>
export default{
    data(){
        return{
            email:"",
            password:""
        }
    },
    methods:{
        async handleLogin(){
            try{
                const response = await fetch('httpe://localhost:5000/api/AdminLogin',{
                    method: 'Post',
                    headers:{
                        'Content-Type':'application/json',
                    },
                })
            }
        }
    }
};
</script>
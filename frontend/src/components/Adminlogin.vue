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
                    bosy: JSON.stringify({
                        email:this.email,
                        password:this.password,
                    }),
                });
                const data = await response.json();

                if(response.ok){
                    localStorage.setItem('token',data.auth_token);
                    this.$router.push('/api/AdminLogin');
                }
                else{
                    this.$router.push('/api/viewer')
                }
            }catch(error){
                this.message = 'Server error. Please try again later';
                console.error(error);
            }
        },
    },
};
</script>
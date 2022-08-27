<script lang="ts">
import { isValidEmail } from "@/utils";

export default {
    data() {
        return {
            email: null,
            password: null,
        }
    },
    methods: {
        async submitForm() {
            if(!this.isValid()) {
                return;
            }

            const formData = new URLSearchParams({
                username: this.email,
                password: this.password
            });

            try {
                const response = await fetch('http://localhost:8000/api/v1/login/access-token', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                });

                if (response.status === 200) {
                    const body = await response.json();
                    
                    localStorage.setItem('token', body.access_token);

                    this.$router.push({ name: 'home' });
                } else {
                    alert('Something went wrong')
                }
            } catch {
                alert('Something went wrong')
            }
        },
        isValid() {
            if (!this.email || !this.password) {
                return false;
            }

            if (!isValidEmail(this.email)) {
                return false;
            }

            return true;
        }
    }
}
</script>

<template>
    <form>
        <h1>Login</h1>

        <div class="form-control">
            <label for="email">Email</label>
            <input type="email" id="email" v-model="email">
        </div>

        <div class="form-control">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password">
        </div>

        <button class="btn" :disabled="!isValid()" @click.prevent="submitForm">Login</button>
    </form>
</template>

<style scoped>
</style>
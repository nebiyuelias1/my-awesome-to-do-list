<script>
import { isValidEmail } from "@/utils";

export default {
    data() {
        return {
            fullName: null,
            email: null,
            password: null,
            confirmPassword: null
        }
    },
    methods: {
        async submitForm(event) {
            if (!this.isValid()) {
                return;
            }
            const formData = {
                email: this.email,
                password: this.password,
                full_name: this.fullName,
                is_active: true,
                is_superuser: false,
            }

            try {
                const response = await fetch('http://localhost:8000/api/v1/users/', {
                    method: 'POST',
                    body: JSON.stringify(formData),
                    headers: {
                        'Content-Type': 'application/json'
                    },
                });

                if (response.status === 200) {
                    this.$router.push({ name: 'login' });
                } else {
                    alert('Something went wrong');
                }
            } catch {
                alert('Something went wrong');
            }
        },
        isValid() {
            if (!this.email || !this.fullName || !this.password || !this.confirmPassword) {
                return false;
            }

            if (!isValidEmail(this.email)) {
                return false;
            }

            if (this.password !== this.confirmPassword) {
                return false;
            }

            return true;
        }
    }
}
</script>

<template>
    <form>
        <h1>Create your account!</h1>

        <div class="form-control">
            <label for="name">Full name</label>
            <input type="text" id="name" v-model="fullName">
        </div>

        <div class="form-control">
            <label for="email">Email</label>
            <input type="email" id="email" v-model="email">
        </div>

        <div class="form-control">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password">
        </div>

        <div class="form-control">
            <label for="confirmpassword">Confirm Password</label>
            <input type="password" id="confirmpassword" v-model="confirmPassword">
        </div>

        <button class="btn" :disabled="!isValid()" @click.prevent="submitForm">Create Account</button>
    </form>

</template>

<style scoped>

</style>
<script>
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
                alert('Something went wrong!');
            }
        },
        isValid() {
            if (!this.email || !this.fullName || !this.password || !this.confirmPassword) {
                return false;
            }

            const regexPattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            if (!regexPattern.test(this.email)) {
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

        <button class="create-button" :disabled="!isValid()" @click.prevent="submitForm">Create Account</button>
    </form>

</template>

<style scoped>
.form-control {
    margin-bottom: 0.25rem;
}

.form-control input {
    display: block;
    padding: 0.5rem;
    border-radius: 8px;
    border: 1px solid;
    width: 100%;
}

.form-control input:focus {
    outline: 1px solid hsla(160, 100%, 37%, 1);
    border: none;
}

.create-button {
    margin-top: 1rem;
    display: block;
    width: 100%;
    padding: 0.5rem;
    background-color: hsla(160, 100%, 37%, 1);
    border: none;
    color: #fff;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
}

.create-button[disabled] {
    background-color: rgba(116, 116, 116, 0.322);
    cursor: unset;
}
</style>
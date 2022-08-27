<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <!-- <header>
    <img alt="Vue logo" class="logo" src="@/assets/task.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="Awesome Todo" />

      <nav>
        <RouterLink to="/signup">Sign Up</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
      </nav>
    </div>
  </header> -->

  <RouterView />
</template>

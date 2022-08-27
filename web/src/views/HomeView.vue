<script lang="ts">

import TheWelcome from '../components/TheWelcome.vue'
import Home from '../components/Home.vue'
import {hasTokenExpired} from '@/utils'

export default {
  methods: {
    isAuthenticated() {
      return !hasTokenExpired();
    }
  },
  components: {
    TheWelcome,
    Home
  }
}

</script>

<template>
  <main>
    <TheWelcome v-if="!isAuthenticated()" />
    <Home  v-if="isAuthenticated()" />
  </main>
</template>

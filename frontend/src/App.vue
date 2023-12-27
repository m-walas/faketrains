<template>
  <v-app>
    <AppBar></AppBar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import AppBar from './components/AppBar.vue';

export default {
  components: {
    AppBar,
  },
};
</script>

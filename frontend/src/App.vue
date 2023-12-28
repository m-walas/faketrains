<template>
  <v-app>
    <AppBar></AppBar>
    <v-main>
      <router-view v-slot="{ Component }">
        <transition name="fade-zoom" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </v-main>
    <Footer></Footer>
  </v-app>
</template>


<style scoped>
.fade-zoom-enter-active, .fade-zoom-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-zoom-enter, .fade-zoom-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
</style>


<script lang="ts">
import AppBar from './components/AppBar.vue';
import Footer from './components/Footer.vue';

export default {
  components: {
    AppBar,
    Footer,
  },
};
</script>

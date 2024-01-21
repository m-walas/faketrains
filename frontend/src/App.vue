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
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.v-main {
  flex: 1;
}

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
import { useAuthStore } from './store/authStore';
import router from './router';

export default {
  data() {
    return {
      authStore: useAuthStore()
    };
  },
  components: {
    AppBar,
    Footer,
  },
  watch: {
    $route(to, from) {
      if (this.authStore.isAuthenticated && to.path === '/auth') {
        router.push('/').catch(err => {
          if (err.name !== 'NavigationDuplicated') {
            throw err;
          }
        });
      }
    },
  },
};
</script>

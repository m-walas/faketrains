<template>
  <v-app>
    <v-parallax src="@/assets/tlo.jpg" height="100%">
      <AppBar></AppBar>
      <v-main class="main-content">
        <router-view v-slot="{ Component }">
          <transition name="fade-zoom" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </v-main>
      <Footer></Footer>
    </v-parallax>
  </v-app>
</template>

<style>
.main-content {
  flex-grow: 1;
}
</style>

<style scoped>
body, html {
  height: 100%;
  margin: 0;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.v-main {
  flex: 1;
  background-color: transparent;
}

.fade-zoom-enter-active,
.fade-zoom-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-zoom-enter,
.fade-zoom-leave-to {
  opacity: 0;
  transform: scale(0.95);
}
</style>

<script lang="ts">
import AppBar from "./components/AppBar.vue";
import Footer from "./components/Footer.vue";
import { useAuthStore } from "./store/authStore";
import router from "./router";

export default {
  data() {
    return {
      authStore: useAuthStore(),
    };
  },
  components: {
    AppBar,
    Footer,
  },
  watch: {
    $route(to, from) {
      if (this.authStore.isAuthenticated && (to.path === "/auth")) {
        router.push("/").catch((err) => {
          if (err.name !== "NavigationDuplicated") {
            throw err;
          }
        });
      }
      if (!this.authStore.isAuthenticated && (to.path === "/profile")) {
        router.push("/auth").catch((err) => {
          if (err.name !== "NavigationDuplicated") {
            throw err;
          }
        });
      }
    },
  },
};
</script>

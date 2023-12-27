<template>
  <v-app-bar app class="animated fadeIn">
    <div class="app-bar-content">
      <v-toolbar-title @click="goToHome" class="app-bar-title">
        FakeTrains
      </v-toolbar-title>

      <Clock></Clock>

      <!-- Warunkowe renderowanie przycisków -->
      <template v-if="authStore.isLoggedIn">
        <div class="user-info">
          <span>{{ authStore.userName }}</span>
          <v-btn icon @click="goToProfile">
            <v-icon>mdi-account</v-icon>
          </v-btn>
          <v-btn icon @click="authStore.logout">
            <v-icon>mdi-logout</v-icon>
          </v-btn>
        </div>
      </template>
      <template v-else>
        <v-btn icon @click="login">
          <v-icon>mdi-login</v-icon>
        </v-btn>
      </template>

      <!-- Przełączanie motywu -->
      <v-btn icon @click="toggleTheme">
        <v-icon>mdi-theme-light-dark</v-icon>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script lang="ts">
import Clock from './Clock.vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store/authStore';

export default {
  components: {
    Clock,
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();

    const goToHome = () => {
      router.push('/');
    };

    const goToProfile = () => {
      router.push('/profile');
    };

    const login = () => {
      router.push('/auth/login');
    };

    const toggleTheme = () => {
      // TODO:  logikę przełączania motywu
    };

    return { authStore, goToHome, goToProfile, login, toggleTheme };
  },
};
</script>

<style scoped>
.app-bar-content {
  display: flex;
  align-items: center;
  width: 100%;
}

.app-bar-title {
  font-family: 'Segoe UI', sans-serif;
  cursor: pointer;
  margin-right: auto;
  margin-left: 50px;
  font-size: 2rem;
}

.user-info {
  display: flex;
  align-items: center;
  margin-right: 15px;
}

.user-info span {
  margin-right: 10px;
  font-weight: bold;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.fadeIn {
  animation-name: fadeIn;
  animation-duration: 1s;
}
</style>

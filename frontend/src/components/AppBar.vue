<template>
  <v-app-bar app class="animated fadeIn">
    <v-toolbar-title @click="goToHome" class="app-bar-title">
      FakeTrains
    </v-toolbar-title>
    <Clock></Clock>

    <v-spacer></v-spacer>

    <template v-if="authStore.isLoggedIn">
      <span class="user-info">{{ authStore.firstName }} {{ authStore.lastName }}</span>
      <v-btn icon @click="goToProfile">
        <v-icon>mdi-account</v-icon>
      </v-btn>
      <v-btn icon @click="handleLogout">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </template>
    <template v-else>
      <v-btn icon @click="login">
        <v-icon>mdi-login</v-icon>
      </v-btn>
    </template>
    
    <v-btn icon @click="toggleTheme">
      <v-icon>mdi-theme-light-dark</v-icon>
    </v-btn>
  </v-app-bar>

  <v-snackbar v-model="snackbarVisible" color="success" top>
    Wylogowano pomyślnie
  </v-snackbar>

</template>

<script lang="ts">
import Clock from './Clock.vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store/authStore';
import { ref } from 'vue';

export default {
  components: {
    Clock,
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const snackbarVisible = ref(false);

    const goToHome = () => {
      router.push('/');
    };

    const goToProfile = () => {
      router.push('/profile');
    };

    const login = () => {
      router.push('/auth');
    };

    const toggleTheme = () => {
      // Logika przełączania motywu
    };

    const handleLogout = () => {
      authStore.logout();
      snackbarVisible.value = true;
      setTimeout(() => {
        snackbarVisible.value = false;
      }, 2000);
    };

    return { authStore, goToHome, goToProfile, login, toggleTheme, snackbarVisible, handleLogout };
  },
};
</script>

<style scoped>
.app-bar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.app-bar-title {
  font-family: 'Segoe UI', sans-serif;
  cursor: pointer;
  font-size: 2rem;
}

.user-info {
  margin-right: 10px;
  font-weight: bold;
}

</style>

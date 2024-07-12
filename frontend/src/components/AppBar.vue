<template>
  <v-app-bar app class="animated fadeIn custom-app-bar">
    <v-toolbar-title @click="goToHome" class="app-bar-title">
      FakeTrains
    </v-toolbar-title>
    <Clock></Clock>

    <v-spacer></v-spacer>

    <div class="user-actions">
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
    </div>
    
  </v-app-bar>

  <v-snackbar v-model="snackbarVisible" color="success" top>
    Wylogowano pomyślnie
  </v-snackbar>

  <v-snackbar v-model="snackbarStore.showMessage" color="success">
    {{ snackbarStore.messageText }}
  </v-snackbar>
</template>

<style scoped>
.custom-app-bar {
  background-color: rgba(0, 0, 0, 0.8) !important;
}

.app-bar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.app-bar-title {
  font-family: 'Segoe UI', sans-serif;
  color: #fff;
  cursor: pointer;
  font-size: 1.2vw;
  transition: color 0.3s ease;
}
/* style for mobile devices */
@media (max-width: 480px) {
  .app-bar-title {
    font-size: 2.8vw;
  }
}
/* style for tablets */
@media (max-width: 768px) {
  .app-bar-title {
    font-size: 3vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2560px) {
  .app-bar-title {
    font-size: 1vw;
  }
}

.app-bar-title:hover {
  color: #ff2770;
}

.user-actions {
  display: flex;
  align-items: center;
}

.user-info {
  margin-right: 1vw;
  font-weight: bold;
  color: #fff;
  font-size: 1.2vw;
}

.v-btn {
  margin-left: 1vw;
  color: #fff;
  transition: transform 0.2s ease-in-out;
}

.v-btn:hover {
  transform: scale(1.1);
}

@media (max-width: 600px) {
  .user-actions {
    flex-direction: column;
  }
  .v-btn {
    margin-top: 0.5vw;
    margin-left: 0; 
  }
}
</style>


<script lang="ts">
import Clock from './Clock.vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store/authStore';
import { ref } from 'vue';
import { useSnackbarStore } from '@/store/snackbarStore'

export default {
  components: {
    Clock,
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const snackbarVisible = ref(false);
    const snackbarStore = useSnackbarStore();

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
      // TODO: do implement
    };

    const handleLogout = () => {
      authStore.logout();
      snackbarVisible.value = true;
      setTimeout(() => {
        snackbarVisible.value = false;
      }, 2000);
    };

    return { authStore, goToHome, goToProfile, login, toggleTheme, snackbarVisible, handleLogout, snackbarStore };
  },
};
</script>
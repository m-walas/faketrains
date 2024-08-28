<template>
  <v-app-bar app class="custom-app-bar">
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
          <v-icon class="icon">mdi-login</v-icon>
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
/* style for mobile devices */
@media (max-width: 480px) {
  .custom-app-bar {
    min-height: 12vw !important;
    padding: 0.5vw !important;
  }
}
/* style for tablets */
@media (max-width: 1028px) {
  .custom-app-bar {
    min-height: 10vw;
    padding: 2vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2260px) {
  .custom-app-bar {
    min-height: 2.2vw;
  }
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
  font-size: 1.5vw;
  transition: color 0.3s ease;
}
/* style for mobile devices */
@media (max-width: 480px) {
  .app-bar-title {
    font-size: 5vw !important;
  }
}
/* style for tablets */
@media (max-width: 1028px) {
  .app-bar-title {
    font-size: 3.5vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2260px) {
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
  justify-content: center;
  padding-right: 2vw;
}

.user-info {
  margin-right: 1vw;
  font-weight: bold;
  color: #fff;
  font-size: 1.2vw;
}
/* style for mobile devices */
@media (max-width: 480px) {
  .user-info {
    font-size: 4vw !important;
  }
}
/* style for tablets */
@media (max-width: 1028px) {
  .user-info {
    font-size: 2.5vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2260px) {
  .user-info {
    font-size: 0.8vw;
  }
}

.v-btn {
  margin-left: 1vw;
  color: #fff;
  transition: transform 0.2s ease-in-out;
}

.v-btn:hover {
  transform: scale(1.1);
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
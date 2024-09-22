<template>
  <v-app-bar
    app
    class="app-bar-custom"
    :style="{ backgroundColor: computedBgColor }"
  >
    <v-toolbar-title class="app-bar-title">
      <span @click="goToHome" class="app-bar-title-text">FakeTrains</span>
    </v-toolbar-title>
    <Clock />

    <v-spacer></v-spacer>

    <div class="app-bar-user-actions">
      <template v-if="authStore.isLoggedIn">
        <span class="app-bar-user-info">{{ authStore.firstName }} {{ authStore.lastName }}</span>
        <v-btn
          icon
          @click="goToProfile"
          class="icon-btn app-bar-icon-btn"
          aria-label="Profile"
          @mousemove="handleMouseMove"
          @mouseleave="resetMousePosition"
        >
          <v-icon>mdi-account</v-icon>
        </v-btn>
        <v-btn
          icon
          @click="handleLogout"
          class="icon-btn app-bar-icon-btn"
          aria-label="Logout"
          @mousemove="handleMouseMove"
          @mouseleave="resetMousePosition"
        >
          <v-icon>mdi-logout</v-icon>
        </v-btn>
      </template>
      <template v-else>
        <v-btn
          icon
          @click="login"
          class="icon-btn app-bar-icon-btn"
          aria-label="Login"
          @mousemove="handleMouseMove"
          @mouseleave="resetMousePosition"
        >
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

<script lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import Clock from './Clock.vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store/authStore';
import { useSnackbarStore } from '@/store/snackbarStore';

export default {
  components: {
    Clock,
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const snackbarVisible = ref(false);
    const snackbarStore = useSnackbarStore();
    const scrollY = ref(0); // current scroll position
    const maxScroll = 90; // max scroll position to start fading

    const goToHome = () => {
      router.push('/');
    };

    const goToProfile = () => {
      router.push('/profile');
    };

    const login = () => {
      router.push('/auth');
    };

    const handleLogout = () => {
      authStore.logout();
      snackbarVisible.value = true;
      setTimeout(() => {
        snackbarVisible.value = false;
      }, 2000);
    };

    // effect for mouse move
    const handleMouseMove = (event: MouseEvent) => {
      const btn = event.currentTarget as HTMLElement;
      const rect = btn.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      btn.style.setProperty('--mouse-x', `${x}%`);
      btn.style.setProperty('--mouse-y', `${y}%`);
    };

    const resetMousePosition = (event: MouseEvent) => {
      const btn = event.currentTarget as HTMLElement;
      btn.style.removeProperty('--mouse-x');
      btn.style.removeProperty('--mouse-y');
    };

    // effect for scroll
    const handleScroll = () => {
      scrollY.value = window.scrollY;
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
    });

    onBeforeUnmount(() => {
      window.removeEventListener('scroll', handleScroll);
    });

    // computed background color
    const computedBgColor = computed(() => {
      const opacityMin = 0.8; // start opacity
      const opacityMax = 0.99; // end opacity
      const scroll = Math.min(scrollY.value, maxScroll);
      const opacity = opacityMin + ((opacityMax - opacityMin) * (scroll / maxScroll));
      return `rgba(0, 0, 0, ${opacity})`;
    });

    return {
      authStore,
      goToHome,
      goToProfile,
      login,
      snackbarVisible,
      handleLogout,
      snackbarStore,
      handleMouseMove,
      resetMousePosition,
      computedBgColor,
    };
  },
};
</script>

<style scoped>
.app-bar-custom {
  --app-bar-text-color: rgba(255, 255, 255, 0.85);
  --app-bar-font-size: clamp(1rem, 2vw, 2rem);
  --app-bar-height: clamp(50px, 5vw, 80px);

  min-height: var(--app-bar-height) !important;
  display: flex;
  align-items: center;
  padding: 0 1rem;
  transition: background-color 0.3s ease;
}

.app-bar-opaque {
  --app-bar-bg-color: rgb(0, 0, 0, 0.99);
}

.app-bar-title {
  font-family: 'Segoe UI', sans-serif;
  color: var(--app-bar-text-color);
  font-size: var(--app-bar-font-size);
  position: relative;
  display: flex;
  align-items: center;
}

.app-bar-title-text {
  cursor: pointer;
  transition: color 0.3s ease;
  position: relative;
  display: inline-block;
}

.app-bar-title-text:hover {
  color: #ff2770;
}

.app-bar-title-text::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0%;
  height: 2px;
  background: #ff2770;
  transition: width 0.3s;
}

.app-bar-title-text:hover::after {
  width: 100%;
}

.app-bar-user-actions {
  display: flex;
  align-items: center;
  margin-right: 1rem;
}

.app-bar-user-info {
  margin-right: 0.5rem;
  font-weight: bold;
  color: var(--app-bar-text-color);
  font-size: clamp(0.8rem, 1.5vw, 1.2rem);
}

.icon-btn {
  color: #fff;
  background-color: transparent !important;
  position: relative;
  transition: transform 0.2s ease-out;
  margin-left: 4px;
  box-shadow: none !important;
  padding: 4px;
}

.app-bar-user-actions .icon-btn:first-of-type {
  margin-left: 0;
}

.icon-btn .v-icon {
  color: #fff;
  font-size: 20px;
}

.icon-btn:hover .v-icon {
  color: #bbb;
}

.icon-btn::before {
  content: '';
  position: absolute;
  top: -5px;
  left: -5px;
  width: calc(100% + 10px);
  height: calc(100% + 10px);
  border: 1px solid rgba(255, 255, 255, 0);
  border-radius: 50%;
  box-sizing: border-box;
  transform: rotate(0deg);
  transition: border-color 0.3s ease, opacity 0.3s ease;
  opacity: 0;
  pointer-events: none;
}

.icon-btn:hover::before {
  border-color: rgba(255, 255, 255, 0.5);
  opacity: 1;
  animation: rotateBorder 10s linear infinite;
}

.icon-btn:hover {
  background-color: transparent !important;
  box-shadow: none !important;
  background-image: none !important;
  transform: translate(
    calc((var(--mouse-x, 50%) - 50%) / 5),
    calc((var(--mouse-y, 50%) - 50%) / 5)
  );
  cursor: none;
}

@keyframes rotateBorder {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 600px) {
  .app-bar-title {
    font-size: clamp(1rem, 5vw, 2rem);
  }

  .app-bar-user-info {
    font-size: clamp(0.8rem, 3vw, 1.2rem);
  }

  .icon-btn .v-icon {
    font-size: 16px;
  }

  .icon-btn {
    padding: 3px;
    margin-left: 3px;
  }
}
</style>

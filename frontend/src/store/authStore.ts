// src/store/authStore.ts
import { defineStore } from 'pinia';

interface AuthState {
  isLoggedIn: boolean;
  username: string;
  firstName: string;
  lastName: string;
}

export const useAuthStore = defineStore({
  id: 'auth',
  state: (): AuthState => ({
    isLoggedIn: false,
    username: '',
    firstName: '',
    lastName: '',
  }),
  getters: {
    isAuthenticated(state): boolean {
      return state.isLoggedIn;
    },
    getUsername(state): string {
      return state.username;
    },
  },
  actions: {
    login(username: string, firstName: string, lastName: string) {
      this.isLoggedIn = true;
      this.username = username;
      this.firstName = firstName;
      this.lastName = lastName;
    },
    logout() {
      this.isLoggedIn = false;
      this.username = '';
      this.firstName = '';
      this.lastName = '';
    }
  },
});

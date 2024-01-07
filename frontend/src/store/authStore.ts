// src/store/authStore.ts
import { defineStore } from 'pinia';
import axios from 'axios';

interface AuthState {
  isLoggedIn: boolean;
  firstName: string;
  lastName: string;
}

export const useAuthStore = defineStore({
  id: 'auth',
  state: (): AuthState => ({
    isLoggedIn: false,
    firstName: '',
    lastName: '',
  }),
  getters: {
    isAuthenticated(state): boolean {
      return state.isLoggedIn;
    },
  },
  actions: {

    login(accessToken: string, refreshToken: string) {
      localStorage.setItem('accessToken', accessToken);
      localStorage.setItem('refreshToken', refreshToken);
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken;

      console.log('Zalogowano')
    
      this.isLoggedIn = true;
    },

    logout() {
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      delete axios.defaults.headers.common['Authorization'];
      this.isLoggedIn = false;
      this.firstName = '';
      this.lastName = '';
      console.log('Wylogowano');
    },

    updateUserInfo(firstName: string, lastName: string){
      this.firstName = firstName.charAt(0).toUpperCase() + firstName.slice(1).toLowerCase();
      this.lastName = lastName.charAt(0).toUpperCase() + lastName.slice(1).toLowerCase();
    },

    initializeAuthState() {
      const accessToken = localStorage.getItem('accessToken');
      if (accessToken) {
        this.isLoggedIn = true;
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken;
      }
    },
  },
});

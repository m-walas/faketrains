// src/store/authStore.ts
import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: false,
    userName: '',
  }),
  actions: {
    checkLoginStatus() {
      const savedState = localStorage.getItem('authState');
      if (savedState) {
        const authState = JSON.parse(savedState);
        this.isLoggedIn = authState.isLoggedIn;
        this.userName = authState.userName;
      } else {
        axios.get('/api/user/status', { withCredentials: true })
          .then(response => {
            this.isLoggedIn = response.data.isLoggedIn;
            this.userName = response.data.firstName + ' ' + response.data.lastName;
            // Aktualizacja localStorage
            localStorage.setItem('authState', JSON.stringify({
              isLoggedIn: this.isLoggedIn,
              userName: this.userName
            }));
          }).catch(error => {
            console.error('Błąd przy sprawdzaniu stanu zalogowania:', error);
          });
      }
    },
    login(userData) {
      axios.post('/api/user/login', userData, { withCredentials: true })
        .then(response => {
          if (response.data.success) {
            this.isLoggedIn = true;
            this.userName = response.data.userName;
            localStorage.setItem('authState', JSON.stringify({
              isLoggedIn: true,
              userName: response.data.userName
            }));
          } else {
            // Obsługa błędu logowania
            console.error('Logowanie nieudane:', response.data);
          }
        }).catch(error => {
          console.error('Błąd logowania:', error);
        });
    },
    logout() {
      axios.post('/api/user/logout', {}, { withCredentials: true })
        .then(() => {
          this.isLoggedIn = false;
          this.userName = '';
          localStorage.removeItem('authState');
        }).catch(error => {
          console.error('Błąd przy wylogowywaniu:', error);
        });
    }
  },
});

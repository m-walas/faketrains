<template>
  <v-card class="pa-4">
    <v-card-text class="text-h3 mb-8 text-center">Logowanie</v-card-text>
    <v-form v-on:keydown.enter="submitForm">
      <v-text-field
        class="input-field"
        density="compact"
        v-model="emailField"
        label="Email"
      ></v-text-field>
      <v-text-field
        class="input-field"
        density="compact"
        v-model="passwordField"
        label="Hasło"
        type="password"
      ></v-text-field>
      <v-row class="ma-1" justify="end" style="max-width: 100%">
        <v-btn @click="submitForm">Zaloguj</v-btn>
      </v-row>
    </v-form>
    <v-card-text class="text-caption pt-4 pb-0 text-center">
      Nie masz konta? Kliknij
      <button class="registerButton" density="compact" @click="navigateToRegister">
        tutaj!
      </button>
    </v-card-text>
  </v-card>
</template>

<script lang="ts">
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store/authStore';
import { ref } from 'vue';

function getCsrfToken() {
  const csrfToken = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1];
  return csrfToken || '';
}

export default {
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const emailField = ref('');
    const passwordField = ref('');

    const submitForm = () => {
      const csrfToken = getCsrfToken();
      const userData = {
        username: emailField.value,
        password: passwordField.value,
      };

      axios.post('/api/user/login', userData, {
        withCredentials: true,
        headers: {
          'X-CSRFToken': csrfToken
        }
      })
      .then(response => {
        if (response.data.success) {
          authStore.login();
          router.push('/');
        } else {
          alert('Błąd logowania: Niepoprawne dane');
        }
      })
      .catch(error => {
        console.error('Błąd połączenia z serwerem:', error);
        alert(`Błąd połączenia z serwerem: ${error.response ? error.response.data.detail : error.message}`);
      });
    };

    const navigateToRegister = () => {
      router.push('/auth/register');
    };

    return { emailField, passwordField, submitForm, navigateToRegister };
  }
};
</script>

<style>

</style>

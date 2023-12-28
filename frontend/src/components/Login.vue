<template>
  <v-card class="pa-4 login-card">
    <v-card-text class="text-h3 mb-8 text-center">Logowanie</v-card-text>
    <v-form v-on:keydown.enter="submitForm">
      <v-text-field class="input-field mb-3" v-model="email" label="Email" outlined dense></v-text-field>
      <v-text-field class="input-field mb-5" v-model="password" label="Hasło" type="password" outlined dense></v-text-field>
      <v-row class="ma-1" justify="end">
        <v-btn class="login-btn" @click="submitForm" color="primary" depressed> Zaloguj </v-btn>
      </v-row>
    </v-form>
  </v-card>
</template>


<style scoped>
.login-card {
  max-width: 500px;
  margin: 50px auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  transition: box-shadow 0.3s ease;
}

.login-card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.input-field {
  transition: box-shadow 0.2s ease-in-out;
}

.input-field:hover {
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

.login-btn {
  transition: transform 0.2s ease-in-out;
}

.login-btn:hover {
  transform: translateY(-2px);
}
</style>


<script lang="ts">
import axios from 'axios';
import { useAuthStore } from '@/store/authStore';
import { ref } from 'vue';
import router from '../router';

export default {
  setup() {
    const email = ref('');
    const password = ref('');
    const authStore = useAuthStore();

    const submitForm = async () => {
      try {
        const response = await axios.post('/api/user/login', {
          username: email.value,
          password: password.value
        });
        if (response.data.success) {
          authStore.login(response.data.username, response.data.firstName, response.data.lastName);
          router.push('/');
        } else {
          alert('Błąd logowania: Niepoprawne dane');
        }
      } catch (error) {
        console.error('Błąd połączenia z serwerem:', error);
        alert('Błąd połączenia z serwerem');
      }
    };

    return { email, password, submitForm };
  }
};
</script>

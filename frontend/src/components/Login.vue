<template>
  <v-card class="pa-4">
    <v-card-text class="text-h3 mb-8 text-center">Logowanie</v-card-text>
    <v-form v-on:keydown.enter="submitForm">
      <v-text-field class="input-field" v-model="email" label="Email"></v-text-field>
      <v-text-field class="input-field" v-model="password" label="Hasło" type="password"></v-text-field>
      <v-row class="ma-1" justify="end">
        <v-btn @click="submitForm">Zaloguj</v-btn>
      </v-row>
    </v-form>
  </v-card>
</template>

<script>
import axios from 'axios';
import { useAuthStore } from '@/store/authStore';
import { ref } from 'vue';

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
          // Przekierowanie lub inna logika
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

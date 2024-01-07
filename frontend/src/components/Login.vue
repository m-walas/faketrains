<template>
  <v-card class="pa-4 login-card">
    <v-card-text class="text-h3 mb-8 text-center">Logowanie</v-card-text>
    <v-alert v-if="showAlert" type="error" class="mb-3" :value="true" v-model="showAlert">
      {{ errorMessage }}
    </v-alert>
    <v-form v-on:keydown.enter="submitForm">
      <v-text-field class="input-field mb-3" v-model="email" label="Email" :rules="emailRules" outlined dense></v-text-field>
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
import { useSnackbarStore } from '@/store/snackbarStore';

export default {
  setup() {
    const email = ref('');
    const emailRules = [
    v => !!v || 'Email jest wymagany',
      v => /.+@.+\..+/.test(v) || 'Podaj prawidłowy adres email',
    ];
    const password = ref('');
    const authStore = useAuthStore();
    const showAlert = ref(false);
    const errorMessage = ref('');
    const snackbarStore = useSnackbarStore();

    const submitForm = async () => {
      try {
        const response = await axios.post('/api/token/', {
          username: email.value,
          password: password.value
        });
        if (response.data.access && response.data.refresh) {
          authStore.login(response.data.access, response.data.refresh);
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access;
          const userInfoResponse = await axios.get('/api/user/profile/');
          authStore.updateUserInfo(
            userInfoResponse.data.firstName,
            userInfoResponse.data.lastName,
          );
          snackbarStore.triggerMessage('Zalogowano pomyślnie');
          router.push('/');
        } else {
          errorMessage.value = 'Błąd logowania: Niepoprawne dane';
          showAlert.value = true;
        }
      } catch (error) {
        if (error.response && error.response.data.error) {
          errorMessage.value = error.response.data.error;
          showAlert.value = true;
        } else {
          console.error('Błąd połączenia z serwerem:', error);
          errorMessage.value = 'Błąd połączenia z serwerem';
          showAlert.value = true;
        }
      }
    };

    return { email, password, submitForm, errorMessage, showAlert, emailRules };
  }
};
</script>

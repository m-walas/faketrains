<template>
  <v-card class="pa-4 login-card">
    <v-card-text class="text-h3 mb-8 text-center">Logowanie</v-card-text>
    
    <v-form v-on:keydown.enter="submitForm" v-model="valid">
      <v-text-field class="input-field mb-3" v-model="email" label="Email" :rules="emailRules" outlined dense></v-text-field>
      <v-text-field class="input-field mb-3" v-model="password" label="Hasło" type="password" :rules="passwordRules" outlined dense></v-text-field>
      <v-alert v-if="showAlert" type="error"  variant="outlined" icon="$info" class="mb-3 mx-auto" style="max-width: 260px" :value="true" v-model="showAlert">
        {{ errorMessage }}
      </v-alert>
      <v-row class="ma-1" justify="end">
        <v-btn class="login-btn" @click="submitForm" color="primary" :disabled="!valid" depressed> Zaloguj  </v-btn>
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

<script>
import axios from 'axios';
import { useAuthStore } from '@/store/authStore';
import { ref } from 'vue';
import router from '../router';
import { useSnackbarStore } from '@/store/snackbarStore';

export default {
  data() {
    return {
      email: '',
      password: '',
      showAlert: false,
      errorMessage: '',
      valid: false,
      emailRules: [
        v => !!v || 'Email jest wymagany',
        v => /.+@.+\..+/.test(v) || 'Podaj prawidłowy adres email',
      ],
      passwordRules: [
        v => !!v || 'Hasło jest wymagane',
      ],
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('/api/token/', {
          username: this.email,
          password: this.password,
        });
        if (response.data.access && response.data.refresh) {
          const authStore = useAuthStore();
          authStore.login(response.data.access, response.data.refresh);
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access;
          const userInfoResponse = await axios.get('/api/user/profile/');
          authStore.updateUserInfo(
            userInfoResponse.data.firstName,
            userInfoResponse.data.lastName,
          );
          const snackbarStore = useSnackbarStore();
          snackbarStore.triggerMessage('Zalogowano pomyślnie');
          router.push('/');
        } else {
          this.errorMessage = 'Niepoprawne dane';
          this.showAlert = true;
        }
      } catch (error) {
        if (axios.isAxiosError(error) && error.response && error.response.status === 401) {
          this.errorMessage = 'Niepoprawne dane';
          this.showAlert = true;
        } else {
          console.error('Error:', error);
          this.errorMessage = 'Błąd połączenia z serwerem';
          this.showAlert = true;
        }
      }
    },
  },
};
</script>

<template>
  <v-card class="pa-4 register-card">
    <v-card-text class="text-h3 mb-8 text-center"> Rejestracja </v-card-text>
    <v-form v-on:keydown.enter="submitForm" v-model="valid">
      <v-text-field
        class="input-field-register"
        density="compact"
        v-model="first_name"
        :rules="firstNameRules"
        label="Imię"
        type="text"
        required
      >
      </v-text-field>
      <v-text-field
        class="input-field-register"
        density="compact"
        v-model="last_name"
        :rules="lastNameRules"
        label="Nazwisko"
        type="text"
        required
      >
      </v-text-field>
      <v-text-field
        class="input-field-register"
        density="compact"
        v-model="email"
        :rules="emailRules"
        label="Email"
        type="email"
        required
      >
      </v-text-field>
      <v-text-field
        class="input-field-register"
        density="compact"
        v-model="password1"
        :rules="passwordRules1"
        label="Hasło"
        type="password"
        required
      >
      </v-text-field>
      <v-text-field
        class="input-field-register"
        density="compact"
        v-model="password2"
        :rules="passwordRules2"
        label="Powtórz hasło"
        type="password"
        required
      >
      </v-text-field>
      <v-row class="ma-1" justify="end" style="max-width: 100%">
        <v-btn class="register-btn" @click="submitForm" color="blue" :disabled="!valid">
          Zarejestruj
        </v-btn>
      </v-row>
    </v-form>
  </v-card>
</template>


<style scoped>
  .input-field-register {
    margin-bottom: 10px;
  }

  .register-card {
    max-width: 500px;
    margin: 50px auto;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    transition: box-shadow 0.3s ease;
  }

  .register-card:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  }

  .register-btn {
    transition: background-color 0.3s ease, transform 0.3s ease;
  }

  .register-btn:hover {
    background-color: #3b82f6;
    transform: translateY(-2px);
  }
</style>


<script lang="ts">
import axios from 'axios';
import { useSnackbarStore } from '../store/snackbarStore';

export default {
  data() {
    return {
      first_name: '',
      last_name: '',
      email: '',
      password1: '',
      password2: '',

      valid: false,
      firstNameRules: [
        v => !!v || 'Imię jest wymagane',
        v=> v?.length >= 2 || 'Imię nie może mieć mniej niż 2 znaki',
        v => v?.length <= 50 || 'Imię nie może być dłuższe niż 50 znaków'
      ],
      lastNameRules: [
        v => !!v || 'Nazwisko jest wymagane',
        v=> v?.length >= 2 || 'Nazwisko nie może mieć mniej niż 2 znaki',
        v => v?.length <= 50 || 'Nazwisko nie może być dłuższe niż 50 znaków'
      ],
      emailRules: [
        v => !!v || 'E-mail jest wymagany',
        v => /.+@.+\..+/.test(v) || 'E-mail musi mieć prawidłowy format'
      ],
      passwordRules1: [
        v => !!v || 'Hasło jest wymagane',
        v =>v?.length >= 8 || 'Hasło musi mięć conajmniej 8 znaków'
      ],
      passwordRules2: [
        v => !!v || 'Hasło jest wymagane',
        v =>v?.length >= 8 || 'Hasło musi mięć conajmniej 8 znaków',
        v => v == this.password1 || 'Hasła nie pasują'
      ],
    };
  },

  setup() {
    const snackbarStore = useSnackbarStore();

    return { snackbarStore }
  },

  methods: {
    async submitForm() {
      if (!this.valid) {
        return;
      }

      try {
        const resp = await axios.post('/api/user/register', {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email, 
          password1: this.password1,
          password2: this.password2
        }, { headers: { 'Authorization': '' } });

        if (resp.data.success) {
          this.snackbarStore.triggerMessage('Konto zostało prawidłowo utworzone.');
          this.$emit('registration-success');
        } else {
          console.log('Error data:', resp.data);
        }
      } catch (error) {
        console.log('Error status:', error.response.status);
        console.log('Error data:', error.response.data);
        console.log('Error headers:', error.response.headers);
      }
    }
  }
};
</script>
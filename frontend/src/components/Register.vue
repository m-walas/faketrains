<template>
  <v-container class="register-container">
  <v-card class="pa-4 register-card">
    <v-card-text class="text-h3 mb-8 text-center"> Register </v-card-text>
    
    <v-form v-on:keydown.enter="submitForm" v-model="valid">
      <v-text-field
        class="input-field"
        density="compact"
        v-model="first_name"
        :rules="firstNameRules"
        label="Imię"
        type="text"
        required
      >
      </v-text-field>
      <v-text-field
        class="input-field"
        density="compact"
        v-model="last_name"
        :rules="lastNameRules"
        label="Nazwisko"
        type="text"
        required
      >
      </v-text-field>
      <v-text-field
        class="input-field"
        density="compact"
        v-model="email"
        :rules="emailRules"
        label="Email"
        type="email"
        required
      >
      </v-text-field>
      <v-text-field
        class="input-field"
        density="compact"
        v-model="password1"
        :rules="passwordRules1"
        label="Hasło"
        type="password"
        required
      >
      </v-text-field>
      <v-text-field
        class="input-field"
        density="compact"
        v-model="password2"
        :rules="passwordRules2"
        label="Powtórz hasło"
        type="password"
        required
      >
      </v-text-field>
      <v-alert v-if="this.serverErrors[0]"
      color="error"
      variant="outlined"
      icon="$info"
      :text=this.serverErrors[0]
      class="mx-auto mb-6"
      style="max-width: 260px"
      ></v-alert>
      <v-row class="ma-1" justify="end" style="max-width: 100%">
        <v-btn class="register-btn" @click="submitForm" color="#ff2770" :disabled="!valid">
          Zarejestruj
        </v-btn>
      </v-row>
    </v-form>
  </v-card>
</v-container>
</template>


<style scoped>
.register-container {
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background: url(../assets/tlo.jpg) no-repeat center center fixed;
  background-size: cover;
}

.register-card {
  width: 400px;
  height: 600px;
  margin: 50px auto;
  padding: 20px;
  box-shadow: 0 0 25px #ff2770;
  border-radius: 8px;
  border: 2px solid #ff2770;
  backdrop-filter: blur(18px);
  color: #fff;
  transition: box-shadow 0.3s ease;
  background-color: rgba(255, 255, 255, 0) !important;
}

.register-card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.input-field {
  background-color: transparent !important;
  margin-top: 20px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 5px;
  transition: box-shadow 0.2s ease-in-out;
}

.input-field:hover {
  box-shadow: 0 0 25px #ff2770;
}

.input-field::placeholder {
  color: #fff;
}

.register-btn {
  transition: background-color 0.3s ease, transform 0.3s ease;
  color: white;
  margin-top: 20px;
}

.register-btn:hover {
  background-color: #ff2770;
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
      snackbarStore: useSnackbarStore(),
      serverErrors: [],

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

  methods: {
    async submitForm() {
      if (!this.valid) {
        return;
      }
      this.serverErrors = []

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
          this.serverErrors[0] = "Błąd z serwerem, spróbuj ponownie później."
        }
      } catch (error) {
        if (error.response && error.response.status) {
          console.log(error.response.data)
          const errorData = JSON.parse(error.response.data.error || '{}');
          for (const fieldName in errorData) {
            if (errorData.hasOwnProperty(fieldName) && Array.isArray(errorData[fieldName])) {
              const firstErrorMessage = errorData[fieldName][0].message;
              this.serverErrors.push(firstErrorMessage)
            }
          }
        } else {
          this.serverErrors[0] = "Błąd z serwerem, spróbuj ponownie później."
        }
      }
    }
  }
};
</script>
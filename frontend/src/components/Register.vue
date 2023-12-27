<template>
  
    <v-card class="pa-4">
      <v-card-text class="text-h3 mb-8 text-center"> Rejestracja </v-card-text>
      <v-form v-on:keydown.enter="submitForm">
        <v-text-field
          class="input-field-register"
          density="compact"
          v-model="firstName"
          label="Imię"
          type="text"
        >
        </v-text-field>
        <v-text-field
          class="input-field-register"
          density="compact"
          v-model="lastName"
          label="Nazwisko"
          type="text"
        >
        </v-text-field>
        <v-text-field
          class="input-field-register"
          density="compact"
          v-model="email"
          label="Email"
          type="email"
        >
        </v-text-field>
        <v-text-field
          class="input-field-register"
          density="compact"
          v-model="password"
          label="Hasło"
          type="password"
        >
        </v-text-field>
        <v-text-field
          class="input-field-register"
          density="compact"
          v-model="confirmPassword"
          label="Powtórz hasło"
          type="password"
        >
        </v-text-field>
        <v-row class="ma-1" justify="end" style="max-width: 100%">
          <v-btn @click="submitForm" color="blue"
            >Zarejestruj</v-btn
          >
        </v-row>
      </v-form>
    </v-card>

</template>

<script lang="ts">



export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      confirmPassword: ''
    };
  },

  methods: {
    async submitForm() {

    }
  }


  
};
</script>
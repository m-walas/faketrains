<template>
    <v-card class="pa-4">
      <v-card-text class="text-h3 mb-8 text-center"> Logowanie </v-card-text>
      <v-form v-on:keydown.enter="submitForm">
        <v-text-field
          class="input-field"
          density="compact"
          v-model="emailField"
          label="Email"
        >
        </v-text-field>
        <v-text-field
          class="input-field"
          density="compact"
          v-model="passwordField"
          label="Hasło"
          type="password"
        >
        </v-text-field>
        <v-row class="ma-1" justify="end" style="max-width: 100%">
          <v-btn @click="submitForm">Zaloguj</v-btn>
        </v-row>
      </v-form>
      <v-card-text class="text-caption pt-4 pb-0 text-center">
        Nie masz konta? Kliknij
        <button
          class="registerButton"
          density="compact"
          @click="navigateToRegister"
        >
          tutaj!
        </button>
      </v-card-text>
    </v-card>

</template>

<script lang="ts">

export default {
  data() {
    return {}
  },

  methods: {

  },
};
</script>
<template>
  <v-container fluid class="d-flex flex-column align-center justify-center">
    <v-fade-transition mode="out-in">
      <Login v-if="showLogin"></Login>
      <Register v-else @registration-success="handleRegistrationSuccess"></Register>
    </v-fade-transition>

    <div class="auth-switch-text">
      <p class="text-center">
        {{ showLogin ? 'Nie masz jeszcze konta?' : 'Masz już konto?' }}
        <span class="auth-switch-button" @click="changeAuthComponent">
          {{ showLogin ? 'Załóż je teraz' : 'Zaloguj się' }}
        </span>
      </p>
    </div>
  </v-container>
</template>


<style scoped>
.auth-switch-text {
  margin-top: 20px;
  max-width: 500px;
  text-align: center;
}

.auth-switch-button {
  cursor: pointer;
  color: #1976D2;
  font-weight: 500;
  text-decoration: underline;
}

.auth-switch-button:hover {
  color: #1258A7;
  text-decoration: none;
}
</style>


<script lang="ts">
import Register from "../components/Register.vue";
import Login from "../components/Login.vue"

export default {
  data() {
    return {
      showLogin: true
    }
  },

  methods: {
    changeAuthComponent() {
      this.showLogin = !this.showLogin
    },

    handleRegistrationSuccess() {
      this.showLogin = true;
    }
  },

  components: {
    Register,
    Login
  }

};
</script>


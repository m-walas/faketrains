<template>
    <v-container fluid class="d-flex column" style="width: fit-content">
        <v-fade-transition mode="out-in">
            <Login v-if="showLogin"></Login>

            <Register v-if="!showLogin" ></Register>
        </v-fade-transition>


    </v-container>  
    <v-card>
            <v-card-text class="text-caption pt-4 pb-0 text-center">
            Masz już konto? Kliknij
            <button
            class="registerButton"
            density="compact"
            @click="changeAuthComponent"
            >
            tutaj
            </button>
            aby sie zalogować!
            </v-card-text>
        </v-card>
</template>
    
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
      }
    },
  
    components: {
      Register,
      Login
    }
  
  };
  </script>


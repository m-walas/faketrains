<template>
        <v-container class="auth-container">
            <v-row justify="center">
                <v-col cols="12" sm="8" md="6" lg="4">
                    <div class="container" id="container" :class="{ 'active': isRegistering }">
                        <div class="form-container sign-up" ref="signUpForm">
                            <h1 class="text-info-signup"> Stwórz konto </h1>
                            <v-card class="auth-card">
                            
                                <v-form v-on:keydown.enter="submitFormRegister" v-model="register_valid">
                                <v-text-field
                                  class="input-field"
                                  density="compact"
                                  v-model="register_first_name"
                                  :rules="register_firstNameRules"
                                  label="Imię"
                                  type="text"
                                  required
                                >
                                </v-text-field>
                                <v-text-field
                                  class="input-field"
                                  density="compact"
                                  v-model="register_last_name"
                                  :rules="register_lastNameRules"
                                  label="Nazwisko"
                                  type="text"
                                  required
                                >
                                </v-text-field>
                                <v-text-field
                                  class="input-field"
                                  density="compact"
                                  v-model="register_email"
                                  :rules="register_emailRules"
                                  label="Email"
                                  type="email"
                                  required
                                >
                                </v-text-field>
                                <div class="field-container">
                                  <v-text-field
                                    ref="registerPasswordField1"
                                    class="input-field"
                                    density="compact"
                                    v-model="register_password1"
                                    :rules="register_passwordRules1"
                                    label="Hasło"
                                    type="password"
                                    required
                                    @focus="checkCapsLockOnFocus"
                                    @keyup="checkCapsLock"
                                    @keydown="checkCapsLock"
                                    @blur="resetCapsLock('register_password1')"
                                  >
                                  </v-text-field>
                                  <v-fade-transition>
                                    <v-alert
                                      v-show="capsLockFields.register_password1"
                                      dense
                                      text
                                      class="caps-lock-alert"
                                    >
                                      Caps Lock jest włączony
                                    </v-alert>
                                  </v-fade-transition>
                                </div>
                                <div class="field-container">
                                  <v-text-field
                                    ref="registerPasswordField2"
                                    class="input-field"
                                    density="compact"
                                    v-model="register_password2"
                                    :rules="register_passwordRules2"
                                    label="Powtórz hasło"
                                    type="password"
                                    required
                                    @focus="checkCapsLockOnFocus"
                                    @keyup="checkCapsLock"
                                    @keydown="checkCapsLock"
                                    @blur="resetCapsLock('register_password2')"
                                  >
                                  </v-text-field>
                                  <v-fade-transition>
                                    <v-alert
                                      v-show="capsLockFields.register_password2"
                                      dense
                                      text
                                      class="caps-lock-alert"                                    
                                    >
                                      Caps Lock jest włączony
                                    </v-alert>
                                  </v-fade-transition>
                                </div>

                                <v-alert v-if="this.serverErrors[0]"
                                  color="error"
                                  variant="outlined"
                                  icon="$info"
                                  :text=this.serverErrors[0]
                                  class="mx-auto mb-6"
                                  style="max-width: 260px"
                                ></v-alert>
                                <v-row class="ma-1" justify="end">
                                    <v-btn class="register-btn" @click="submitFormRegister" :disabled="!register_valid">
                                    Zarejestruj
                                    </v-btn>
                                </v-row>
                                </v-form>
                            </v-card>
                        </div> 

                        <div class="form-container sign-in" ref="signInForm">
                            <h1 class="text-info-signin"> Zaloguj się </h1>
                            <v-card class="auth-card">

                                <v-form v-on:keydown.enter="submitFormLogin" v-model="login_valid">
                                    <v-text-field 
                                      class="input-field mb-3" 
                                      v-model="login_email" label="Email" 
                                      :rules="login_emailRules" 
                                      outlined 
                                      dense
                                    ></v-text-field>
                                    <div class="field-container">
                                      <v-text-field 
                                        ref="loginPasswordField"
                                        class="input-field mb-3" 
                                        v-model="login_password" 
                                        label="Hasło" 
                                        type="password" 
                                        :rules="login_passwordRules" 
                                        outlined 
                                        dense
                                        @focus="checkCapsLockOnFocus"
                                        @keyup="checkCapsLock"
                                        @keydown="checkCapsLock"
                                        @blur="resetCapsLock('login_password')"
                                      ></v-text-field>
                                      <v-fade-transition>
                                        <v-alert
                                          v-show="capsLockFields.login_password"
                                          dense
                                          text
                                          class="caps-lock-alert"                                    
                                        >
                                          Caps Lock jest włączony
                                        </v-alert>
                                      </v-fade-transition>
                                    </div>
                                    <v-alert v-if="showAlert" type="error"  variant="outlined" icon="$info" class="mb-3 mx-auto" style="max-width: 260px" :value="true" v-model="showAlert">
                                    {{ errorMessage }}
                                    </v-alert>
                                    <v-row class="ma-1" justify="end">
                                        <v-btn class="login-btn" @click="submitFormLogin" :disabled="!login_valid" depressed> Zaloguj </v-btn>
                                    </v-row>
                                </v-form>
                            </v-card>
                        </div>

                        <div class="toggle-container">
                            <div class="toggle">
                                <div class="toggle-panel toggle-left">
                                    <h1>Witaj z powrotem!</h1>
                                    <p>Wprowadź dane logowania i podróżuj z FakeTrains po całym świecie!</p>
                                    <button class="hidden" id="login" @click="isRegistering = false">Login</button>
                                </div>
                                <div class="toggle-panel toggle-right">
                                    <h1>Cześć!</h1>
                                    <p>Załóż konto i podróżuj razem z FakeTrains po całym świecie!</p>
                                    <button class="hidden" id="register" @click="isRegistering = true">Register</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </v-col>
            </v-row>
        </v-container>
</template>

<script>
import axios from 'axios';
import { useAuthStore } from '@/store/authStore';
import { ref } from 'vue';
import router from '../router';
import { useSnackbarStore } from '@/store/snackbarStore';

export default {
  data() {
      return {
      isRegistering: false,
      capsLockFields: {
          login_password: false,
          register_password1: false,
          register_password2: false
      },
      // login form
      login_email: '',
      login_password: '',
      showAlert: false,
      errorMessage: '',
      login_valid: false,
      login_emailRules: [
      v => !!v || 'Email jest wymagany',
      v => /.+@.+\..+/.test(v) || 'Podaj prawidłowy adres email',
      ],
      login_passwordRules: [
      v => !!v || 'Hasło jest wymagane',
      ],
      // register form
      register_first_name: '',
      register_last_name: '',
      register_email: '',
      register_password1: '',
      register_password2: '',
      snackbarStore: useSnackbarStore(),
      serverErrors: [],

      register_valid: false,

      register_firstNameRules: [
      v => !!v || 'Imię jest wymagane',
      v=> v?.length >= 2 || 'Imię nie może mieć mniej niż 2 znaki',
      v => v?.length <= 50 || 'Imię nie może być dłuższe niż 50 znaków'
      ],
      register_lastNameRules: [
      v => !!v || 'Nazwisko jest wymagane',
      v=> v?.length >= 2 || 'Nazwisko nie może mieć mniej niż 2 znaki',
      v => v?.length <= 50 || 'Nazwisko nie może być dłuższe niż 50 znaków'
      ],
      register_emailRules: [
      v => !!v || 'E-mail jest wymagany',
      v => /.+@.+\..+/.test(v) || 'E-mail musi mieć prawidłowy format'
      ],
      register_passwordRules1: [
      v => !!v || 'Hasło jest wymagane',
      v =>v?.length >= 8 || 'Hasło musi mięć co najmniej 8 znaków'
      ],
      register_passwordRules2: [
      v => !!v || 'Hasło jest wymagane',
      v =>v?.length >= 8 || 'Hasło musi mięć co najmniej 8 znaków',
      v => v == this.register_password1 || 'Hasła nie pasują'
      ],
      };
  },
  methods: {
    async submitFormLogin() {
      try {
      const response = await axios.post('/api/token/', {
          username: this.login_email,
          password: this.login_password,
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
    async submitFormRegister() {
      if (!this.register_valid) {
      return;
      }
      this.serverErrors = []

      try {
      const resp = await axios.post('/api/user/register', {
          first_name: this.register_first_name,
          last_name: this.register_last_name,
          email: this.register_email, 
          password1: this.register_password1,
          password2: this.register_password2
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
    },
    checkCapsLockOnFocus(event) {
      const isCapsLock = event.getModifierState('CapsLock');
      if (event.target === this.$refs.registerPasswordField1.$el.querySelector('input')) {
        this.capsLockFields.register_password1 = isCapsLock;
        this.capsLockFields.register_password2 = false;
        this.capsLockFields.login_password = false;
      } else if (event.target === this.$refs.registerPasswordField2.$el.querySelector('input')) {
        this.capsLockFields.register_password2 = isCapsLock;
        this.capsLockFields.register_password1 = false;
        this.capsLockFields.login_password = false;
      } else if (event.target === this.$refs.loginPasswordField.$el.querySelector('input')) {
        this.capsLockFields.login_password = isCapsLock;
        this.capsLockFields.register_password1 = false;
        this.capsLockFields.register_password2 = false;
      }
    },
    checkCapsLock(event) {
      const isCapsLock = event.getModifierState('CapsLock');
      if (document.activeElement === this.$refs.registerPasswordField1.$el.querySelector('input')) {
        this.capsLockFields.register_password1 = isCapsLock;
      } else if (document.activeElement === this.$refs.registerPasswordField2.$el.querySelector('input')) {
        this.capsLockFields.register_password2 = isCapsLock;
      } else if (document.activeElement === this.$refs.loginPasswordField.$el.querySelector('input')) {
        this.capsLockFields.login_password = isCapsLock;
      }
    },
    resetCapsLock(field) {
      this.capsLockFields[field] = false;
    },
    globalCapsLockCheck(event) {
      const isCapsLock = event.getModifierState('CapsLock');
      this.capsLockFields.register_password1 = isCapsLock && (document.activeElement === this.$refs.registerPasswordField1.$el.querySelector('input'));
      this.capsLockFields.register_password2 = isCapsLock && (document.activeElement === this.$refs.registerPasswordField2.$el.querySelector('input'));
      this.capsLockFields.login_password = isCapsLock && (document.activeElement === this.$refs.loginPasswordField.$el.querySelector('input'));
    },
  },
  mounted() {
    document.addEventListener('keydown', this.globalCapsLockCheck);
    document.addEventListener('keyup', this.globalCapsLockCheck);
  },
  beforeDestroy() {
    document.removeEventListener('keydown', this.globalCapsLockCheck);
    document.removeEventListener('keyup', this.globalCapsLockCheck);
  },
};
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background: transparent !important;
  height: 100vh;
}

.container {
  background-color: rgb(0, 0, 0, 0.8);
  border-radius: 30px;
  box-shadow: 0 5px 15px rgb(0, 0, 0, 0.35);
  position: relative;
  overflow: hidden;
  width: 90vw;
  max-width: 1100px;
  min-height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (min-aspect-ratio: 21/9) {
  .container {
    max-width: 900px;
  }
}

.container p{
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.3px;
  margin: 20px 0;
}

.container button{
  background-color: #ff2770;
  color: #fff;
  font-size: 0.7vw;
  padding: 1vw 4.2vw;
  border: 1px solid transparent;
  border-radius: 8px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-top: 1vw;
  cursor: pointer;
}
/* style for mobile devices */
@media (max-width: 480px) {
  .container button {
    font-size: 1.9vw !important;
    padding: 1.5vw 5vw !important;
  }
}
/* style for tablets */
@media (max-width: 1028px) {
  .container button {
    font-size: 1.3vw;
    padding: 0.9vw 4vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2260px) {
  .container button {
    font-size: 0.4vw;
    padding: 0.7vw 3vw;
  }
}

.container button.hidden{
  background-color: transparent;
  border-color: #fff;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  display: flex;
}

.sign-in {
  left: 0;
  width: 50%;
  z-index: 2;
}

.container.active .sign-in {
  transform: translateX(100%);
}

.sign-up {
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}

.container.active .sign-up {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: move 0.6s;
}

@keyframes move{
  0%, 49.99%{
      opacity: 0;
      z-index: 1;
  }
  50%, 100%{
      opacity: 1;
      z-index: 5;
  }
}

.toggle-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: all 0.6s ease-in-out;
  border-radius: 150px 0 0 100px;
  z-index: 1000;
}

.container.active .toggle-container {
  transform: translateX(-100%);
  border-radius: 0 150px 100px 0;
}

.toggle {
  background-color: #ff2770;
  height: 100%;
  background: linear-gradient(to right, #f483a9, #e6004c);
  color: #fff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: all 0.6s ease-in-out;
}

.container.active .toggle {
  transform: translateX(50%);
}

.toggle-panel {
  position: absolute;
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 30px;
  text-align: center;
  top: 0;
  transform: translateX(0);
  transition: all 0.6s ease-in-out;
}

.toggle-left {
  transform: translateX(-200%);
}

.container.active .toggle-left {
  transform: translateX(0);
}

.toggle-right {
  right: 0;
  transform: translateX(0);
}

.container.active .toggle-right {
  transform: translateX(200%);
}

.auth-card {
  background-color: rgb(0, 0, 0);
  backdrop-filter: blur(10px);
  padding: 20px;
  max-width: 400px;
  width: 100%;
  border: none;
  border-radius: 15px;
  box-shadow: 0 0 0 rgba(0, 0, 0, 0);
}

.input-field {
  background-color: transparent;
  border-radius: 8px;
  transition: box-shadow 0.2s ease-in-out;
  color: #fff;
  font-size: 13px;
  padding: 2px 5px;
}

.input-field:hover {
  box-shadow: 0 0 25px #ff2770;
}

.input-field::placeholder {
  color: #666;  
}

.register-btn, .login-btn {
  background-color: #ff2770;
  color: #fff;
  font-size: 2vw;
  padding: 1vw 4vw;
  border: 1px solid transparent;
  border-radius: 8px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-top: 1vw;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

@media (max-width: 600px) {
  .register-btn, .login-btn {
    font-size: 3vw;
  }
}

.register-btn.hidden, .login-btn.hidden {
  background-color: transparent;
  border-color: #fff
}

.register-btn:hover, .login-btn:hover {
  background-color: #b8033f;
  transform: translateY(-2px);
}

.text-info-signup, .text-info-signin{
  color: #ff2770;
  font-size: 1.2vw;
  margin-left: 1vw;
  padding: 15px;
  background-color: transparent;
}
@media (max-width: 2100px) {
  .text-info-signup, .text-info-signin {
    font-size: 2.5vw;
  }
}
@media (max-width: 1400px) {
  .text-info-signup, .text-info-signin {
    font-size: 3.5vw;
  }
}
@media (max-width: 700px) {
  .text-info-signup, .text-info-signin {
    font-size: 4vw;
  }
}

.field-container {
  position: relative;
  width: 100%;
}

.caps-lock-alert {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  width: 100%;
  text-align: center;
  font-size: 12px;
  padding: 3px;
  background-color: rgba(255, 39, 111, 0.3);
  color: #fff;
  border-radius: 0 0 8px 8px;
  backdrop-filter: blur(3px);
}

</style>
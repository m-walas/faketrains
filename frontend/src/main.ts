import { createApp } from 'vue';
import axios from 'axios';

// Components
import App from "./App.vue";
import router from './router';
import vuetify from './plugins/vuetify';
import { pinia } from './store';

// ! EDIT HERE if working locally !
// axios.defaults.baseURL = 'http://localhost:8000/';
axios.defaults.baseURL = 'https://django.mwalas.pl/';
console.log('axios.defaults.baseURL: ', axios.defaults.baseURL);

const app = createApp(App);
app.config.globalProperties.$axios = axios;

app.use(router);
app.use(vuetify);
app.use(pinia);

app.mount('#app');
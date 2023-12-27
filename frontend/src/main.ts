import { createApp } from 'vue';
import axios from 'axios';

// Components
import App from "./App.vue";
import router from './router';
import vuetify from './plugins/vuetify';
import { pinia } from './store';

axios.defaults.baseURL = 'https://django.mwalas.pl/';

const app = createApp(App);
app.config.globalProperties.$axios = axios;

app.use(router);
app.use(vuetify);
app.use(pinia);

app.mount('#app');
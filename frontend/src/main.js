import { createApp } from 'vue'; // Importuj createApp z vue
import App from './App.vue';
import VueNativeSock from 'vue-native-websocket';

const app = createApp(App); // Utwórz instancję aplikacji

app.mount('#app');

app.config.productionTip = false; // Ustaw config na instancji aplikacji

const options = {
  format: 'json',
};

app.use(VueNativeSock, 'ws://localhost:8000/ws/train_seat/', options); // Użyj app do konfiguracji VueNativeSock

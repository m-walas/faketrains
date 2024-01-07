import { createApp } from 'vue';
import axios from 'axios';
import App from "./App.vue";
import router from './router';
import vuetify from './plugins/vuetify';
import { pinia } from './store';
import { useAuthStore } from '@/store/authStore';
import { createPinia } from 'pinia';

let isTokenBeingRefreshed = false;
let didTokenRefreshFail = false;

// ! EDIT HERE if working locally !
// axios.defaults.baseURL = 'http://localhost:8000/';
axios.defaults.baseURL = 'https://django.mwalas.pl/';
console.log('axios.defaults.baseURL: ', axios.defaults.baseURL);

const app = createApp(App);
const pinia = createPinia();
app.use(pinia);
app.config.globalProperties.$axios = axios;

const accessToken = localStorage.getItem('accessToken');
const authStore = useAuthStore();
authStore.initializeAuthState();

if (accessToken) {
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken;
    authStore.isLoggedIn = true;

    verifyTokenAndUpdateUserInfo();
}

async function verifyTokenAndUpdateUserInfo() {
    if (didTokenRefreshFail) {
        return;
    }

    try {
        const userInfoResponse = await axios.get('/api/user/profile/');
        authStore.updateUserInfo(
            userInfoResponse.data.firstName,
            userInfoResponse.data.lastName
        );
        console.log('informacje o użytkowniku zaktualizowane.')
    } catch (error) {
        if (error.response && error.response.status === 401 && !isTokenBeingRefreshed) {
            await refreshTokenAndRetry();
        } else {
            console.error('Błąd weryfikacji tokena: ', error);
            authStore.logout();
            router.push('/auth');
        }
    }
}

async function refreshTokenAndRetry() {
    isTokenBeingRefreshed = true;

    const refreshToken = localStorage.getItem('refreshToken');
    if (refreshToken) {
        try {
            const refreshResponse = await axios.post('/api/token/refresh/', {
                refresh: refreshToken
            });
            localStorage.setItem('accessToken', refreshResponse.data.access);
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + refreshResponse.data.access;
            authStore.isLoggedIn = true;

            await verifyTokenAndUpdateUserInfo();
        } catch (error) {
            console.error('Błąd odświeżania tokena: ', error);
            didTokenRefreshFail = true;
            authStore.logout();
            router.push('/');
        }
    } else {
        authStore.logout();
        router.push('/');
    }
    
    isTokenBeingRefreshed = false;
}

app.use(router);
app.use(vuetify);
app.mount('#app');
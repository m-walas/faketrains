import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

// Views
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
import SeatSelectionView from '../views/SeatSelectionView.vue';
import RoutesView from '../views/RoutesView.vue';
import AuthView from '../views/AuthView.vue'


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/auth/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/auth',
    name: 'Login',
    component: AuthView,
  },
  
  {
    path: '/auth/register',
    name: 'Register',
    component: RegisterView,
  },
  {
    path: '/seat-selection',
    name: 'SeatSelection',
    component: SeatSelectionView,
  },
  {
    path: '/routes',
    name: 'Routes',
    component: RoutesView,
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

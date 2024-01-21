import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

// Views
import HomeView from '../views/HomeView.vue';
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
    path: '/auth',
    name: 'Auth',
    component: AuthView,
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

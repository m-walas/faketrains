import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

// Views
import HomeView from '../views/HomeView.vue';
import RoutesView from '../views/RoutesView.vue';
import AuthView from '../views/AuthView.vue';
import ProfileView from '../views/ProfileView.vue'

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
    path: '/routes',
    name: 'Routes',
    component: RoutesView,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
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

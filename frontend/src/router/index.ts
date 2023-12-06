// Composables
import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import AuthView from "../views/AuthView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/auth",
      name: "auth",
      component: AuthView
    },

    
    {
      path: "/:catchAll(.*)",
      redirect: "/"
  },
  ]
})


export default router

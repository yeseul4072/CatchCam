import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main.vue'
import Login from '../views/member/Login.vue'
import Signup from '../views/member/Signup.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
      path: '/login',
      name: 'Login',
      component: Login
  },
  {
      path: '/signup',
      name: 'Signup',
      component: Signup
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

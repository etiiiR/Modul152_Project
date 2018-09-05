import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Künstler from '@/components/Künstler'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Kuenstler',
      name: 'Künslter',
      component: Künstler
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    }

  ]
})

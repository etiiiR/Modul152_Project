import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Künstler from '@/components/Künstler'
import Upload from '@/components/Upload'
import Login from '@/components/Login'
import Created from '@/components/Created'
import YourSongs from '@/components/YourSongs'

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
    },
    {
      path: '/Uploade',
      name: 'Upload',
      component: Upload
    },
    {
      path: '/created',
      name: 'Created',
      component: Created
    },
    {
      path: '/yourSongs',
      name: 'YourSongs',
      component: YourSongs
    }

  ]
})

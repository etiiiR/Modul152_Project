// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMq from 'vue-mq'
import APlayer from '@moefe/vue-aplayer'
import axios from './backend/vue-axios/'

Vue.use(ElementUI)
Vue.config.productionTip = false

Vue.use(APlayer, {
  defaultCover: 'https://github.com/u3u.png', // set the default cover
  productionTip: false, // disable console output
  fixedoptional: true,
  listFolded: true,
  listMaxHeight: 200,
  theme: ' #ebd0c2',
  autoplay: false
})

Vue.use(VueMq, {
  breakpoints: {
    not: 222,
    mobile: 600,
    tablet: 800,
    laptop: 1250,
    desktop: Infinity
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  axios,
  template: '<App/>',
  components: { App }
})

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMq from 'vue-mq'

Vue.use(ElementUI)
Vue.config.productionTip = false

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
  template: '<App/>',
  components: { App }
})

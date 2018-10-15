// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMq from 'vue-mq'
import APlayer from '@moefe/vue-aplayer'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuex from 'vuex'

Vue.use(ElementUI)
Vue.use(Vuex)
Vue.use(VueAxios, axios)
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

const store = new Vuex.Store({
  state: {
    all: [],
    name: '',
    artist: '',
    url: '',
    cover: '',
    lrc: '',
    audio: [],
    qualityoption: ''
  },
  mutations: {
    addSongtoPlaylist (state) {
      let b = {
        name: this.state.name,
        artist: this.state.artist,
        url: this.state.url,
        cover: this.state.cover,
        lrc: this.state.lrc
      }
      this.state.audio.push(b)
    }
  },
  computed: {
    musics () {
      return this.$store.state.audio
    }
  }
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  store,
  components: { App }
})

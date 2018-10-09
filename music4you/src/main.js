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
    name: '',
    artist: '',
    url: '',
    cover: '',
    lrc: '',
    audio: [
      {
        name: 'Iam the NOONE',
        artist: 'Justin XXX',
        url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
        cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
        lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc'
      }
    ]
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
      console.log(this.state.audio)
    }
  },
  computed: {
    musics () {
      return this.$store.state.audio
    }
  }
})

store.commit('addSongtoPlaylist')

store.commit('addSongtoPlaylist')

store.commit('addSongtoPlaylist')

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  store,
  components: { App }
})

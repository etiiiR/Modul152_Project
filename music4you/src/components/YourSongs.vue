<template>
    <div>
        <el-row>
  <el-col :span="5" v-for="item in data" :key="item" :offset="index > 0 ? 1 : 1">
    <el-card :body-style="{ padding: '0px' }">
      <img v-bind:src="item.image" class="image">
      <div style="padding: 14px;">
        <span>{{ item.title }}</span>
        <div class="bottom clearfix">
          <time class="time" style="float: left">{{ item.date_created }}</time>
          <p style="font-size: 2px">URL</p>
          <el-button @click="addPlaylist(item.id, item.title, item.Genere, item.image, item.upload, item.lyrics, item.upload_128, item.upload_192)" v-bind="url='mellos'" style="float: right" round>Add to Playlist</el-button>
        </div>
      </div>
    </el-card>
    <p></p>
  </el-col>
</el-row>
    </div>
</template>



<style>
  .time {
    font-size: 13px;
    color: #999;
  }

  .el-main {
      line-height: 2;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      data: [],
      name: '',
      url: 'hello',
      msg: 'Enjoy',
      currentDate: '2018-10-09'
    }
  },
  methods: {
    addPlaylist (key, title, genere, image, upload, lyrcis, upload128, upload192) {
      alert(this.$store.state.qualityoption)
      this.$store.state.name = title
      this.$store.state.artist = genere
      if (this.$store.state.qualityoption == 0) {
        this.$store.state.url = upload
      } else if (this.$store.state.qualityoption == 1) {
        this.$store.state.url = upload192
      } else if (this.$store.state.qualityoption == 2) {
        this.$store.state.url = upload128
      } else {
        console.log('audio quality konnte nicht geladen werden')
      }
      this.$store.state.cover = image
      this.$store.state.lrc = lyrcis
      this.$store.commit('addSongtoPlaylist')
    }
  },
  created () {
    axios.get('http://localhost:8001/musics')
    .then((response) => {
      this.data = response.data
    })
  }
}
</script>

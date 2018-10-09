<template>
    <div>
        <el-row>
  <el-col :span="5" v-for="(o, index) in 8" :key="o" :offset="index > 0 ? 1 : 1">
    <el-card :body-style="{ padding: '0px' }">
      <img src="../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg" class="image">
      <div style="padding: 14px;">
        <span>{{ name }}</span>
        <div class="bottom clearfix">
          <time class="time" style="float: left">{{ currentDate }}</time>
          <p style="font-size: 1px">URL</p>
          <el-button @click="addPlaylist(o)" v-bind="url='mellos'" style="float: right" round>Add to Playlist</el-button>
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
      name: '',
      url: 'hello',
      msg: 'Enjoy',
      currentDate: '2018-10-09'
    }
  },
  methods: {
    addPlaylist (key) {
      alert(key)
    }
  },
  created () {
    axios.get('http://localhost:8001/musics')
    .then((response) => {
      console.log(response.data)
      console.log(response.status)
      console.log(response.statusText)
      console.log(response.headers)
      console.log(response.config)
    })
  }
}
</script>

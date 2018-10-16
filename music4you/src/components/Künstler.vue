<template>
  <el-carousel :interval="4000" type="card" height="450px">
    <el-carousel-item v-for="bild in bilder" :key="bild">
      <img v-bind:src="bild.image" width="75%" />
    </el-carousel-item>
  </el-carousel>
</template>

<script>
// only axios get and show the image in the carousell
import axios from 'axios'
export default {
  data () {
    return {
      bilder: []
    }
  },
  methods: {},
  created () {
    axios.get('http://localhost:8001/musics')
    .then((response) => {
      this.bilder = response.data
    })
  }
}
</script>


<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.0;
    line-height: 450px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: rgba(0,0,0,0.0)
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: rgba(0,0,0,0.0)
  }
</style>
<template>
  <el-carousel :interval="4000" type="card" height="450px">
    <el-carousel-item v-for="item in 6" :key="item">
      <img v-bind:src="image" width="75%" />
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
  data () {
    return {
      image: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg'
    }
  },
  methods: {}
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
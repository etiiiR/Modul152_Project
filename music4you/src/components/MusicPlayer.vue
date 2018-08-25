<template>
  
  <div class="hello">
    <aplayer :audio="audio" :lrc-type="3" />
  </div>
</template>

<script>
export default {
  data () {
    return {
      audio: {
        name: 'ヒビカセ',
        artist: 'れをる',
        url: 'http://pdacsgxq7.bkt.clouddn.com/mp3/hibikase.mp3',
        cover: 'http://p1.music.126.net/cZPx3peGTuWEI_GaZB5CDg==/8892850045794893.jpg?param=300y300',
        lrc: 'http://pdacsgxq7.bkt.clouddn.com/lrc/hibikase.lrc'
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.aplayer {
    margin: 0px;
}



</style>

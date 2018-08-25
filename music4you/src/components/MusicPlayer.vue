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
        name: 'Iam the One',
        artist: 'Justin Biber',
        url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
        cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
        lrc: '../../media/lyrics/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayn_DoGcdAl.lrc'
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

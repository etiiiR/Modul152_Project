<template>
  
  <div class="hello">
    <aplayer :audio="audio" :lrc-type="3" />
  </div>
</template>

<script>
export default {
  data () {
    return {
      audio: [
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: this.randomColor()
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: this.randomColor()
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: 'ebd0c2'
        },
        {
          name: 'Iam the One',
          artist: 'Justin Biber',
          url: '../../media/mp3/2018/08/25/DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayne.mp3',
          cover: '../../media/image/2018/08/25/dj-khaleds-im-the-one-music-video-features-justin-bieber-lil-wayne-chan_jBLNSlb.jpg',
          lrc: '../../media/lyrics/2018/08/25/DJ-Khaled-Im-the-One-ft.-Justin-Bieber-Quavo-Chance-the-Rapper-Lil-Wayne.lrc',
          theme: '#46718b'
        }]
    }
  },
  methods: {
    randomColor () {
      return `#${((Math.random() * 0xffffff) << 0).toString(16)}`
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.aplayer {
    margin: 0px;
    background-color: rgb(250, 250, 250);
}
.aplayer {
  background-color: rgb(250, 250, 250)
}

.aplayer-lrc:before {
  background-color: rgb(250, 250, 250)
}

.aplayer-lrc {
  background-color: rgb(250, 250, 250);
}


</style>

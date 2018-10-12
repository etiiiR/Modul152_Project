<template>
  
  <div class="hello">
    <aplayer :audio="audio" :lrc-type="3" />
  </div>
</template>

<script>
export default {
  data () {
    return {
      audio: this.$store.state.audio
    }
  },
  methods: {
    randomColor () {
      return `#${((Math.random() * 0xffffff) << 0).toString(16)}`
    },
    addmusic () {
      for (let i = 0; i < this.$store.state.audio.length; i++) {
        console.log(i)
        alert(i)
      }
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

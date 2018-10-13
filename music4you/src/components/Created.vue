<template>
    <div style="">
        <h1>Your song is about to be</h1>
        <h2>Uploaded and Converted</h2>
        <div id="app">
        <el-progress v-if="precentece < 100" type="circle"  show-text="false" :percentage="precentece"></el-progress>
        <el-progress v-else type="circle" :percentage="100" status="success"></el-progress>
</div>
    </div>
</template>

<style>
.el-message {
  z-index: 10001;
}
</style>

<script>
export default {
  data () {
    return {
      precentece: 0,
      isRunning: false,
      interval: null,
      count: 0
    }
  },
  mounted  () {
    if (this.isRunning) {
      clearInterval(this.interval)
    } else {
      this.interval = setInterval(this.incrementTime, 100)
    }
    this.isRunning = !this.isRunning
  },
  methods: {
    incrementTime () {
      if (this.precentece < 100) {
        this.precentece = parseInt(this.precentece) + 2
      } else if (this.precentece === 100 && this.count === 0) {
        this.open2()
        this.count = 1
      }
    },
    open2 () {
      this.$message({
        message: 'Congrats, Your song is uploaded',
        type: 'success'
      })
    }
  }
}
</script>

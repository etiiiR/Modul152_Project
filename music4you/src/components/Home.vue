<template>
  
  <div class="hello">
    <h1 v-if="$mq !== 'mobile'" style="line-height: 2px;">Welcome on Music4You on the {{ $mq }} version</h1>
    <el-row :gutter="20">
    <el-col  :span="this.span"><div class="grid-content bg-purple">
      <el-card class="box-card">
        <div class="text item">
          Songs
        </div>
    </el-card>
    </div></el-col>
    <el-col :span="this.span"><div class="grid-content bg-purple">
    <el-card class="box-card">
        <div class="text item">
          Login
        </div>
    </el-card>
    </div></el-col>
    <el-col :span="this.span"><div class="grid-content bg-purple">
    <el-card class="box-card">
        <div class="text item">
          Login
        </div>
    </el-card>
    </div></el-col>
    <el-col :span="this.span"><div class="grid-content bg-purple">
    <el-card class="box-card">
        <div class="text item">
          Upload
        </div>
    </el-card>
    </div></el-col>
    <el-col :span="this.span"><div class="grid-content bg-purple">
    <el-card class="box-card">
        <div class="text item">
          Login
        </div>
    </el-card>
    </div></el-col>
    </el-row>
    <div class="el-scrollbar__bar is-horizontal"><div class="el-scrollbar__thumb" style="transform: translateX(0%);"></div></div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      span: 6,
      msg: 'Enjoy'
    }
  },
  mounted () {
    if (this.$mq === 'mobile') {
      this.span = 12
    } else if (this.$mq === 'tablet') {
      this.span = 8
    } else {
      this.span = 6
    }
  },
  updated () {
    if (this.$mq === 'mobile') {
      this.span = 12
    } else if (this.$mq === 'tablet') {
      this.span = 8
    } else {
      this.span = 6
    }
  },
  methods: {}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}

.el-main {
      text-align: center;
}

.el-card {
  margin-top: 20px; 
}


</style>

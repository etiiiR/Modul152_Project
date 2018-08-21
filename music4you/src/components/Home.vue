<template>
  
  <div class="hello">
    <h1>Welcome on Music4You</h1>
    <el-button type="primary" icon="el-icon-edit"></el-button>
    <el-button type="primary" icon="el-icon-share"></el-button>
    <el-button type="primary" icon="el-icon-delete"></el-button>
    <el-button type="primary" icon="el-icon-search">Search</el-button>
    <el-button type="primary">Upload<i class="el-icon-upload el-icon-right"></i></el-button>
    <h1>{{ msg }}</h1>
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
      msg: 'Enjoy'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}



</style>

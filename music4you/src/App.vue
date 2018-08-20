<template>
  <div id="app">
    <el-container>
      <el-aside width="200px">
        <sidebar></sidebar>
      </el-aside>
    <el-container>
      <el-header>
        <navbar></navbar>
      </el-header>
      <el-main>
        <img class="logo" src="./assets/logo.png">
        <br>
        <img class="logo" src="./assets/dj.png">
        <router-view/>
        <p>
        Welcome to your Django - Vue.js app!
        </p>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
    </el-container>
  </div>
</template>




<script>
import Navbar from './components/Navbar.vue'
import Sidebar from './components/Sidebar.vue'

export default {
  name: 'app',
  components: {
    'navbar': Navbar,
    'sidebar': Sidebar
  }
}
</script>

<style>

  body {
    margin: 0;
  }

  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
.logo {
  width: 100px;
  height: 100px
}
</style>

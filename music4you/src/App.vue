<template>
  <div id="app">
    <div id="not" v-if="$mq === 'not'">
      <h2>Screen Resolution to low</h2>
      <h3>Your Device is not Supported im sorry please contact the:</h3>
      <h5>etienne.roulet@gibmit.ch</h5>
    </div>
    <el-container v-if="$mq !== 'not'" >
      <el-aside width="auto">
      </el-aside>
      <sidebar></sidebar>
    <el-container>
      <el-header>
        <navbar></navbar>
      </el-header>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
    </el-container>
     <div id="footer">
        <musicplayer></musicplayer>
      </div>
  </div>
</template>




<script>
import Navbar from './components/Navbar.vue'
import Sidebar from './components/Sidebar.vue'
import Footers from './components/Footers.vue'
import MusicPlayer from './components/MusicPlayer.vue'

export default {
  name: 'app',
  components: {
    'navbar': Navbar,
    'sidebar': Sidebar,
    'footers': Footers,
    'musicplayer': MusicPlayer
  }
}
</script>

<style>

  .aplayer-music {
  color: black;
  }

  .aplayer.aplayer-withlist .aplayer-list {
    color: black;
  }

  .aplayer .aplayer-list li .aplayer-list-index {
    float: left;
  }


  body {
    margin: 0;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }

  .el-header {
    z-index: 10000;
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
    padding: 0;
    position: sticky;
    top: 0px;
  }

  .sidebar_border {
    background-color:rgb(250, 250, 250);
  }


  .el-menu-vertical-demo:not(.el-menu--collapse) {
    background-color:rgb(250, 250, 250);
  }
  
  #footer {
    border-top: solid 2px #e6e6e6;
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    color: white;
    text-align: center;
  }
  
  .el-main {
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  .el-container {
    padding-bottom: 70px;
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
  height: 100px;
}


.el-menu-vertical-demo {
  border: none;
}

.el-menu--collapse {
  background-color: rgb(250, 250, 250);
}

.el-menu--horizontal {
  background-color: rgb(250, 250, 250);
}

.el-container>.is-vertical {
  min-height: 100vh;
}

#not{
  background-color:color;
  text-decoration-color: white;
  padding-right:30px;
}


@media only screen and (max-width: 600px) {

}

.el-input__inner {
  border-radius: 20px;
}




</style>

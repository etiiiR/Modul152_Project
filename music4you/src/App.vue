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
        <p>
        Welcome to your Django - Vue.js app!
        </p>
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

  body {
    margin: 0;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  }

  .el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
    padding: 0;
    position: sticky;
    top: 0px;
  }

  
  #footer {
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



/* Customize website's scrollbar like Mac OS
Not supports in Firefox and IE */

/* total width */
body::-webkit-scrollbar {
    background-color:#fff;
    width:16px
}

/* background of the scrollbar except button or resizer */
body::-webkit-scrollbar-track {
    background-color:#fff
}

/* scrollbar itself */
body::-webkit-scrollbar-thumb {
    background-color:#babac0;
    border-radius:16px;
    border:4px solid #fff
}

/* set button(top and bottom of the scrollbar) */
body::-webkit-scrollbar-button {display:none}

</style>

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
        <fab v-if="$mq === 'mobile'" :actions="fabActions"
       @cache="cache"
       @alertMe="alert"
      ></fab>
         <p id="notss" v-if="$mq === 'tablet'" style="margin-top: 80px"></p>
        <p id="nots" v-if="$mq === 'mobile'" style="margin-top: 100px"></p>
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
// component imports globaly
import Navbar from './components/Navbar.vue'
import Sidebar from './components/Sidebar.vue'
import Footers from './components/Footers.vue'
import MusicPlayer from './components/MusicPlayer.vue'
import Login from './components/Login.vue'
import fab from 'vue-fab'

// components using
export default {
  name: 'app',
  components: {
    'navbar': Navbar,
    'sidebar': Sidebar,
    'footers': Footers,
    'musicplayer': MusicPlayer,
    'login': Login,
    fab
  },
  data () {
    // fab data
    return {
      bgColor: '#778899',
      position: 'top-right',
      fabActions: [
        {
          name: 'cache',
          icon: 'cached'
        },
        {
          name: 'alertMe',
          icon: 'add_alert'
        }
      ]
    }
  },
  methods: {
    // fab methods
    cache () {
      alert('Dieses Feature ist noch nicht implementiert bitte nur auf den unteren Button clicken um auf den Home screen zu laden')
    },
    alert () {
      alert('alert')
      this.$router.push({ path: '/' })
    }
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
    z-index: 1999;
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

.fab-main {
  margin-bottom: 80px;
}


</style>

<template>
<div class="sidebar_border" v-if="$mq !== 'mobile'" >
    <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" :collapse-transition=true  @close="handleOpen" :collapse="isCollapse">
        
        <router-link tag="none" to="/" >
        <el-menu-item id="el-logo"  index="1">
            <img class="el-logo" v-bind:src='img' height="30px">
            <span slot="title">Music4You</span>
        </el-menu-item>
        </router-link>

        <router-link tag="none" to="/kuenstler/" >
        <el-menu-item index="2">
            <i class="el-icon-sort"></i>
            <span slot="title">Künstler</span>
        </el-menu-item>
        </router-link>


        <router-link tag="none" to="/yourSongs/" >
        <el-menu-item index="3">
            <i class="el-icon-menu"></i>
            <span slot="title">Deine Songs</span>
        </el-menu-item>
        </router-link>

        <router-link tag="none" to="/login/" >
        <el-menu-item index="4">
            <i class="el-icon-document"></i>
            <span slot="title">Login</span>
        </el-menu-item>
        </router-link>

        <router-link tag="none" to="/uploade/" >
        <el-menu-item index="5">
            <i class="el-icon-upload2"></i>
            <span slot="title">Uploade</span>
        </el-menu-item>
        </router-link>

        <router-link tag="none" to="/settings" >
        <el-menu-item index="6">
            <i class="el-icon-setting"></i>
            <span slot="title">Settings</span>
        </el-menu-item>
        </router-link>

        <el-menu-item v-if="$mq !== 'tablet'" index="6" @click="toggle" >
            <i class="el-icon-d-arrow-right"></i>
        </el-menu-item>
    </el-menu>
</div>
</template>

<style>
li a {
    text-decoration: none;
}


.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 25vh;
    min-width: 0px;
    min-height: auto;
    position: sticky;
    top: 0px;
}

.el-menu--collapse {
    position: sticky;
    top: 0px;
}

.sidebar_border {
    border-right: solid 1px #e6e6e6;
}

#el-logo  {
    height: 61px;
    border: none;
}

.el-menu-item {
    margin-bottom: 0vh;
}


</style>

<script>
export default {
  data () {
    return {
      isCollapse: true,
      img: 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/ITunes_12.2_logo.png/600px-ITunes_12.2_logo.png'
    }
  },
  methods: {
    toggle () {
      this.isCollapse = !this.isCollapse
    },
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

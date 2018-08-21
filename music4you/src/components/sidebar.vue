<template>
<div>
    <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
        <el-menu-item index="1">
            <img class="el-logo" v-bind:src='img' height="30px">
            <span slot="title">Music4You</span>
        </el-menu-item>
        <el-submenu index="2">
            <template slot="title">
                <i class="el-icon-location"></i>
                <span slot="title">Nach Title</span>
            </template>
            <el-menu-item-group>
                <span slot="title">Group One</span>
                <el-menu-item index="2-1">item one</el-menu-item>
                <el-menu-item index="2-2">item two</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="Group Two">
                <el-menu-item index="2-3">item three</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="2-4">
                <span slot="title">item four</span>
                <el-menu-item index="2-4-1">item one</el-menu-item>
            </el-submenu>
        </el-submenu>
        <el-menu-item index="3">
            <i class="el-icon-menu"></i>
            <span slot="title">Nach Künstler</span>
        </el-menu-item>
        <el-menu-item index="4" disabled>
            <i class="el-icon-document"></i>
            <span slot="title">Nach Genere</span>
        </el-menu-item>
        <el-menu-item index="5">
            <i class="el-icon-setting"></i>
            <span slot="title">Top Hits</span>
        </el-menu-item>
        <el-menu-item index="6">
            <i class="el-icon-setting"></i>
            <span slot="title">Settings</span>
        </el-menu-item>
        <el-menu-item index="6" @click="toggle" >
            <i class="el-icon-d-arrow-right"></i>
        </el-menu-item>
    </el-menu>
</div>
</template>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: auto;
    min-height: auto;
}

.el-aside {
    background-color: white;
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
      console.log('toggle')
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

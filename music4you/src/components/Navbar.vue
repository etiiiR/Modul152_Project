<template>
<div>
<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1">Processing Center</el-menu-item>
  <el-submenu index="2">
    <template slot="title">Workspace</template>
    <el-menu-item index="2-1">item one</el-menu-item>
    <el-menu-item index="2-2">item two</el-menu-item>
    <el-menu-item index="2-3">item three</el-menu-item>
    <el-submenu index="2-4">
      <template slot="title">item four</template>
      <el-menu-item index="2-4-1">item one</el-menu-item>
      <el-menu-item index="2-4-2">item two</el-menu-item>
      <el-menu-item index="2-4-3">item three</el-menu-item>
    </el-submenu>
  </el-submenu>
  <el-menu-item index="3">Info</el-menu-item>
  <el-menu-item index="4" disabled >Account</el-menu-item>
  <el-autocomplete
  v-model="state4"
  :fetch-suggestions="querySearchAsync"
  placeholder="Please input"
  @select="handleSelect"
></el-autocomplete>
</el-menu>
</div>
</template>


<script>
  export default {
    data () {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        links: [],
        state4: '',
        timeout: null
      }
    },
    methods: {
      handleSelects (key, keyPath) {
        console.log(key, keyPath)
      },
      loadAll () {
        return [
          { 'value': 'vue', 'link': 'https://github.com/vuejs/vue' },
          { 'value': 'element', 'link': 'https://github.com/ElemeFE/element' },
          { 'value': 'cooking', 'link': 'https://github.com/ElemeFE/cooking' },
          { 'value': 'mint-ui', 'link': 'https://github.com/ElemeFE/mint-ui' },
          { 'value': 'vuex', 'link': 'https://github.com/vuejs/vuex' },
          { 'value': 'vue-router', 'link': 'https://github.com/vuejs/vue-router' },
          { 'value': 'babel', 'link': 'https://github.com/babel/babel' }
        ]
      },
      querySearchAsync (queryString, cb) {
        var links = this.links
        var results = queryString ? links.filter(this.createFilter(queryString)) : links

        clearTimeout(this.timeout)
        this.timeout = setTimeout(() => {
          cb(results)
        }, 3000 * Math.random())
      },
      createFilter (queryString) {
        return (link) => {
          return (link.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
        }
      },
      handleSelect (item) {
        console.log(item)
      }
    },
    mounted () {
      this.links = this.loadAll()
    }
  }
</script>

<style scoped>
.el-menu-item {
  float: right;
  height: 60px;
}
</style>

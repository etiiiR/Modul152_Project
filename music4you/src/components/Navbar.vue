<template>
<div>
<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
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
  <el-menu-item index="4" >Account</el-menu-item>
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
  import axios from 'axios'
  export default {
    data () {
      return {
        datama: [],
        searchvalues: [],
        activeIndex: '1',
        activeIndex2: '1',
        links: [],
        state4: '',
        timeout: 5
      }
    },
    methods: {
      handleSelects (key, keyPath) {
        console.log(key, keyPath)
      },
      loadAll () {
        return this.searchvalues
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
        this.$store.state.name = item.title
        this.$store.state.artist = item.Genere
        this.$store.state.url = item.upload
        this.$store.state.cover = item.image
        this.$store.state.lrc = item.lyrcis
        this.$store.commit('addSongtoPlaylist')
        console.log(this.$store.state.audio)
      }
    },
    beforeMount () {
      axios.get('http://localhost:8001/musics')
        .then((response) => {
          this.datama = response.data
          console.log(this.datama)
          let searchvalues = []
          this.datama.forEach(function (element) {
            console.log(element)
            let b = {
              'value': element.title, 'link': element.id, 'id': element.id, 'title': element.title, 'Genere': element.Genere, 'image': element.image, 'lyrcis': element.lyrcis, 'upload': element.upload, 'upload128': element.upload128, 'upload192': element.upload192
            }
            console.log(b)
            searchvalues.push(b)
          })
          this.searchvalues = searchvalues
          console.log(this.searchvalues)
          this.links = this.searchvalues
        })
    },
    mounted () {
      this.links = this.loadAll()
    },
    addPlaylist (key, title, genere, image, upload, lyrcis, upload128, upload192) {
      this.$store.state.name = title
      this.$store.state.artist = genere
      this.$store.state.url = upload
      this.$store.state.cover = image
      this.$store.state.lrc = lyrcis
      this.$store.commit('addSongtoPlaylist')
      console.log(this.$store.state.audio)
    }
  }
</script>



<style scoped>
.el-menu-item {
  float: right;
  height: 60px;
}
</style>

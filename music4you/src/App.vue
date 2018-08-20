<template>
  <div id="app">
    <navbar></navbar>
    <img class="logo" src="./assets/logo.png">
    <br>
    <img class="logo" src="./assets/dj.png">
    <router-view/>
    <p>
      Welcome to your Django - Vue.js app!
    </p>
  </div>
</template>




<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'app',
  components: {
    'navbar': Navbar
  }
}
</script>

<style>
html {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

#app {
  color: #2c3e50;
  margin-top: -100px;
  max-width: 600px;
  font-family: Source Sans Pro, Helvetica, Arial, sans-serif;
  text-align: center;
}

#app a {
  color: #42b983;
  text-decoration: none;
}

.logo {
  width: 100px;
  height: 100px
}
</style>

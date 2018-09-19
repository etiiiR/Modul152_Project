<template>
<div class="form_song">
  <el-form ref="form" :model="form" label-width="120px">
     <el-form-item label="title">
    <el-input v-model="form.title"></el-input>
  </el-form-item>
   <el-form-item label="genere">
    <el-input v-model="form.Genere"></el-input>
  </el-form-item>
  
  <el-form-item>
    <el-button type="primary" @click="onSubmit">Create</el-button>
    <el-button>Cancel</el-button>
  </el-form-item>
  </el-form>
</div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      form: {
          title: '',
          Genere: '',

        }
      }
    },
    methods: {
      onSubmit() {
        alert(this.form.title)
        alert(this.form.Genere)
        axios.post('http://localhost:8000/musics/create/', {
        title: this.form.title,
        Genere: this.form.Genere
        }).then(response => 200)
    }  
  }
}
</script>

<style>
.form_song {
  max-width: 1200px;
  padding-top: 10%;
  padding-left: 15%;
  padding-right: 15%;
}

.el-main {
  text-align: left;
  line-height: 2;
}
</style>

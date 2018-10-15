<template>
<div class="form_song">
  <el-form ref="form" :model="form" label-width="120px">
     <el-form-item label="title">
    <el-input v-model="form.title"></el-input>
  </el-form-item>
   <el-form-item label="artist">
    <el-input v-model="form.Genere"></el-input>
  </el-form-item>
  
  <el-form-item>
  <input type="file" @change="onFileChanged">
  </el-form-item>
  <el-form-item>
  <input type="file" @change="onFileChanged1">
  (Uploads müssen in 320 kbit erfolgen...)
  </el-form-item>
  <el-form-item>
  <input type="file" @change="onFileChanged2">
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
      image: null,
      upload: null,
      lyrics: null,
      form: {
        title: '',
        Genere: ''
      }
    }
  },
  methods: {
    open6() {
      this.$notify.error({
        title: 'Error',
        message: 'filled not correctly the from, Upload faild try to fill up again'
      });
    },
    onFileChanged (event) {
      this.image = event.target.files[0]
    },
    onFileChanged1 (event) {
      this.upload = event.target.files[0]
    },
    onFileChanged2 (event) {
      this.lyrics = event.target.files[0]
    },
    onSubmit () {
      const formData = new FormData()
      formData.append('title', this.form.title)
      formData.append('Genere', this.form.Genere)
      formData.append('image', this.image)
      formData.append('upload', this.upload)
      formData.append('lyrics', this.lyrics)
      axios.post('http://localhost:8001/musics/create/',
        formData,
        { headers: {
          'Content-Type': 'multipart/form-data'
        }
        })
        .then(response => {
          this.image = null
          this.upload = null
          this.lyrics = null
          this.form.title = null
          this.form.Genere = null
          this.$router.push({ path: '/created/' })
        })
        .catch(error => {
          this.open6()
        })
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
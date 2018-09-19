<template>
<div class="form_song">
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>Files
        <input type="file" id="files" ref="files" multiple v-on:change="handleFilesUpload()"/>
      </label>
    </div>
    <div class="large-12 medium-12 small-12 cell">
      <div v-for="(file, key) in files" class="file-listing">{{ file.name }} <span class="remove-file" v-on:click="removeFile( key )">Remove</span></div>
    </div>
    <br>
    <div class="large-12 medium-12 small-12 cell">
      <button v-on:click="addFiles()">Add Files</button>
    </div>
    <br>
    <div class="large-12 medium-12 small-12 cell">
      <button v-on:click="submitFiles()">Submit</button>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      files: []
    }
  },
  methods: {
    /*
          Adds a file
        */
    addFiles () {
      this.$refs.files.click()
    },
    /*
          Submits files to the server
        */
    submitFiles () {
      /*
              Initialize the form data
            */
      let formData = new FormData()
      /*
              Iteate over any file sent over appending the files
              to the form data.
            */
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i]
        formData.append('files[' + i + ']', file)
      }
      /*
              Make the request to the POST /select-files URL
            */
      axios
        .post('http://localhost:8000/musics/create', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function () {
          console.log('SUCCESS!!')
        })
        .catch(function () {
          console.log('FAILURE!!')
        })
    },
    /*
          Handles the uploading of files
        */
    handleFilesUpload () {
      let uploadedFiles = this.$refs.files.files
      alert(uploadedFiles)
      /*
              Adds the uploaded file to the files array
            */
      for (var i = 0; i < uploadedFiles.length; i++) {
        this.files.push(uploadedFiles[i])
      }
    },
    /*
          Removes a select file the user has uploaded
        */
    removeFile (key) {
      this.files.splice(key, 1)
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

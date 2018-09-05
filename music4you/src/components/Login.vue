<template>
    <div class="login">
        <el-form ref="form" :model="form" label-width="120px">
            <el-form-item label="Username">
            <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item type="Email" label="email">
            <el-input type="email" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item type="Password" label="Password">
            <el-input type="password" v-model="form.password"></el-input>
            </el-form-item>
             <el-form-item>
            <el-button type="primary" @click="onSubmit">Create</el-button>
            <el-button @click="resetForm('ruleForm2')">Reset</el-button>
            </el-form-item>
        </el-form>
    </div>

</template>

<script>
  export default {
    data () {
      return {
        form: {
          name: '',
          password: '',
          email: ''
        }
      }
    },
    methods: {
      onSubmit () {
        alert(this.form.name, this.form.password, this.form.email)
        console.log( "username:", this.form.name, "email:", this.form.email, "password:", this.form.password, )
        this.$http.post('/rest-auth/login/', { username: this.form.name, email: this.form.email, password: this.form.password, })
        .then(request => this.loginSuccessful(request))
        .catch(() => this.loginFailed())
      },
      loginSuccessful (req) {
        if (!req.data.token) {
          this.loginFailed()
          return
        }
        localStorage.token = req.data.token
        this.error = false
        this.$router.replace(this.$route.query.redirect || '/authors')
      },
      loginFailed () {
        this.error = 'Login failed!'
        delete localStorage.token
      }
    }
  }
</script>

<style>

.el-form {
}
</style>


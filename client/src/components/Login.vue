
<template>
  <div class="hello">
    <img alt="Vue logo" src="../assets/1232.png">
    <h1>{{ msg }}</h1>
    <div>
      <el-input placeholder="Username"  clearable class="input_style"></el-input>
    </div>
    <div>
      <el-input placeholder="Password"  clearable class="input_style"></el-input>
    </div>
    <div>
      <el-button type="primary" class="login_style">Login</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  h1{
    font-size: 24px;
   margin-top:-50px;
  }
  .input_style {
    width: 200px;
    margin-bottom: 10px;
  }
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

<template>
  <div id="app">
    <Recommendation/>
  </div>
</template>

<script>
import Recommendation from './components/Recommendation.vue'
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

export default {
  name: 'App',
  components: {
    Recommendation
  }
}
</script>

<style lang="scss">
@import './assets/custom.scss';
@import '../node_modules/bootstrap/scss/bootstrap.scss';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

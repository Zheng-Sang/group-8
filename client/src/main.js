import router from './routes/index'

import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false

Vue.use(ElementUI)

new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  router,
  render: h => h(App),
}).$mount('#app')

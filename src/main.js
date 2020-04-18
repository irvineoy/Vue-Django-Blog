import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false;
Vue.prototype.$http = axios;
// Vue.prototype.$router = router;
axios.defaults.baseURL = 'http://127.0.0.1:8000';
// var io = require('socket.io')(server, { origins: '*:*'});



new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

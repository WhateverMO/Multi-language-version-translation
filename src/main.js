import Vue from 'vue'
import App from './App.vue';
import VueI18n from 'vue-i18n'
import router from '@/router'
import store from '@/store'
import ElemnetUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios';
Vue.config.productionTip = false
axios.defaults.withCredentials = true;
Vue.use(ElemnetUI);
Vue.use(VueI18n);


const i18n = new VueI18n({
  locale: 'cn',
  messages: {
    'cn': require('./lang/cn'),
    'us': require('./lang/us')
  }
})
const app = new Vue({
  render: h => h(App),
  router,
  i18n,
  store,
  beforeCreate() {
    Vue.prototype.$bus = this
  },

})
app.$mount('#app')


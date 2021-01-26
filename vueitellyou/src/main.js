import Vue from "vue";
import App from "./App.vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import router from "./router";
import axios from "axios";

axios.defaults.baseURL = "https://api.gd97.xyz/";
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";

Vue.prototype.$axios = axios;

Vue.use(ElementUI);
Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");

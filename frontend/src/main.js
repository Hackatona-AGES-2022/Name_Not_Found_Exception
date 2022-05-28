import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
  data: () => ({
    toolbarTitle: '',
    isToolbarVisible: false
  }),
  methods: {
    showToolbar(title) {
      this.toolbarTitle = title;
      this.isToolbarVisible = true;
    },
    hideToolbar() {
      this.isToolbarVisible = false;
    }
  }
}).$mount("#app");

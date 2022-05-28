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
    isToolbarVisible: false,
    isSnackbarVisible: false,
    snackbarText: "",
  }),
  methods: {
    showToolbar(title) {
      this.toolbarTitle = title;
      this.isToolbarVisible = true;
    },
    hideToolbar() {
      this.isToolbarVisible = false;
    },
    showSnackbar(text) {
      this.snackbarText = text;
      this.isSnackbarVisible = true;
    }
  }
}).$mount("#app");

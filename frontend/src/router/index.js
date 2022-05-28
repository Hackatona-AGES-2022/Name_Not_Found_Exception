import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import CreateSale from '../views/CreateSale.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/sales/create",
    name: "Create Sale",
    component: CreateSale,
  },
];

const router = new VueRouter({
  routes,
});

export default router;

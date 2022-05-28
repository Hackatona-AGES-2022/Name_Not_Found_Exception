import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import CreateSale from '../views/CreateSale.vue';
import Login from "../views/Login.vue";

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
  {
    path: "/pre-sign-in",
    name: "Pre Sign In",
    component: Login
  },
  {
    path: "/sign-in",
    name: "Sign in",
    component: Login
  },
];

const router = new VueRouter({
  routes,
});

export default router;

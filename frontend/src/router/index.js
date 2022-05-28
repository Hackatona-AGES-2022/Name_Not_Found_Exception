import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import CreateSale from '../views/CreateSale.vue';
import Login from "../views/Login.vue";
import SignUp from "../views/SignUp.vue";
import SignUpStore from "../views/SignUpStore.vue";
import SignUpUser from "../views/SignUpUser.vue";
import UserCart from '../views/UserCart.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Pre Sign In",
    component: Login,
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
  {
    path: "/user/home",
    name: "User Home",
    component: Home,
  },
  {
    path: "/store/home",
    name: "Store Home",
    component: Home
  },
  {
    path: "/store/sales/create",
    name: "Create Sale",
    component: CreateSale,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  }, {
    path: "/sign-up-store",
    name: "SignUpStore",
    component: SignUpStore,
  },
  {
    path: "/sign-up-user",
    name: "SignUpUser",
    component: SignUpUser,
  },
  {
    path: "/user/cart/",
    name: "User Cart",
    component: UserCart,
  }
];

const router = new VueRouter({
  routes,
});

export default router;

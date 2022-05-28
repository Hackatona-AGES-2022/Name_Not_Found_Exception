import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import CreateSale from '../views/CreateSale.vue';
import Login from "../views/Login.vue";
import { getUserType } from '../service/UserService';

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
    component: Home
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
];

const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  const preSignIn = 'Pre Sign In';
  if (to.name !== preSignIn) {
    const type = getUserType();
    if (to.path.startsWith(`/${type}`)) {
      next()
    } else {
      next({ name: preSignIn });
    }
  } else {
    next();
  }
})

export default router;

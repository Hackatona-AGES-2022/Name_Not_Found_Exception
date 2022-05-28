import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import CreateSale from '../views/CreateSale.vue';
import Login from "../views/Login.vue";
import SignUp from "../views/SignUp.vue";
import SignUpStore from "../views/SignUpStore.vue";
import SignUpUser from "../views/SignUpUser.vue";
import UserCart from '../views/UserCart.vue';
import { getUserType } from "../service/UserService";

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
    meta: {
      middleware: userMiddleware
    }
  },
  {
    path: "/store/home",
    name: "Store Home",
    component: Home,
    meta: {
      middleware: storeMiddleware
    }
  },
  {
    path: "/store/sales/create",
    name: "Create Sale",
    component: CreateSale,
    meta: {
      middleware: storeMiddleware
    }
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

function userMiddleware({ next }) {
  const type = getUserType();
  if (type === 'user') {
    next();
  }
  return next({ name: 'Spre Sign In' });
}

function storeMiddleware({ next }) {
  const type = getUserType();
  if (type === 'store') {
    next();
  }
  return next({ name: 'Spre Sign In' });
}

export default router;

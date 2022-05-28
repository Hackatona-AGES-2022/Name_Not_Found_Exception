import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import SignUp from "../views/SignUp.vue";
import SignUpStore from "../views/SignUpStore.vue";
import SignUpUser from "../views/SignUpUser.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/SignUp",
    name: "SignUp",
    component: SignUp,
  },{
    path: "/SignUpStore",
    name: "SignUpStore",
    component: SignUpStore,
  },{
    path: "/SignUpUser",
    name: "SignUpUser",
    component: SignUpUser,
  },
];

const router = new VueRouter({
  routes,
});

export default router;

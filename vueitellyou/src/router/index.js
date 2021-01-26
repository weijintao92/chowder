// import { resolve } from "core-js/fn/promise";
import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: resolve => require(["../views/Home.vue"], resolve)
  }
];

const router = new VueRouter({
  routes
});

export default router;

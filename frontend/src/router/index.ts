import { createRouter, createWebHashHistory } from "vue-router";

const Home = () => import("../pages/Home.vue");
const Login = () => import("../pages/Login.vue");
const New_Flux = () => import("../pages/New_Flux.vue")

const routes = [
  { path: "/", component: Login, meta: { title: "Login" } },
  { path: "/home", component: Home, meta: { title: "Home"} },
  { path: "/new_flux", component: New_Flux, meta: { title: "New_Flux"} },

];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.afterEach((to) => {
  // document.title = `${to.meta.title}`;

  document.title = `Login`;
  window.scrollTo(0, 0);
});

export default router;

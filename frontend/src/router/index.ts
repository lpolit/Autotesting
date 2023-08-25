import { createRouter, createWebHashHistory } from "vue-router";

// const Home = () => import("../pages/Home.vue");
// const Tabla = () => import("../pages/Tabla.vue");
// const Modal = () => import("../pages/Modal.vue");
const NotFound = () => import("../pages/NotFound.vue");

const routes = [
  // { path: "/", component: Home, meta: { title: "Inicio" } },
  // { path: "/tabla", component: Tabla, meta: { title: "Tabla" } },
  // { path: "/modal", component: Modal, meta: { title: "Modal" } },
  {
    path: "/notfound",
    component: NotFound,
    meta: { title: "NotFound Example" },
  },
  { path: "/:pathMatch(.*)*", name: "not-found", component: NotFound },
  { path: "/:pathMatch(.*)", name: "bad-not-found", component: NotFound },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.afterEach((to) => {
  // document.title = `${to.meta.title}`;

  document.title = `Inicio`;
  window.scrollTo(0, 0);
});

export default router;

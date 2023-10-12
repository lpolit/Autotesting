import { createRouter, createWebHashHistory } from "vue-router";

const Home_Flux = () => import("../pages/Home_Flux.vue");
const Home_Project = () => import("../pages/Home_Project.vue");
const Login = () => import("../pages/Login.vue");
const Register = () => import("../pages/Register.vue");
const Reset_Password = () => import("../pages/Reset_Password.vue");
const Change_Password = () => import("../pages/Change_Password.vue");
const New_Flux = () => import("../pages/New_Flux.vue")

const routes = [
  { path: "/", component: Login, meta: { title: "Login" } },
  { path: "/change", name:"change", component: Change_Password, meta: { title: "Cambiar contraseña"},props:true },
  { path: "/reset", name:"reset", component: Reset_Password, meta: { title: "Recuperar contraseña"},props:true },
  { path: "/register", name:"register", component: Register, meta: { title: "Registro"},props:true },
  { path: "/home_flux", name:"home_flux", component: Home_Flux, meta: { title: "Mis Flujos"},props:true },
  { path: "/home_project", name:"home_project", component: Home_Project, meta: { title: "Mis Projectos"},props: true },
  { path: "/new_flux", name:"new_flux", component: New_Flux, meta: { title: "Flujo"} },

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

import { createApp } from "vue";
import { createPinia } from "pinia";
import router from "./router";
import App from "./App.vue";
import Header from "@/pages/Header.vue";
import Footer from "@/pages/Footer.vue";
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import Notifications from '@kyvg/vue3-notification'



// import { EdaVue } from "@eda/vue";
// import "@eda/style/dist/css/all.css";
// import "@eda/vue/dist/eda-vue.css";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
const app = createApp(App);
app.component('Header', Header)
app.component('Footer', Footer)
app.use(pinia);
app.use(router);
app.use(Notifications);
app.mount("#app");


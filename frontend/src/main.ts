import { createApp } from "vue";
import { createPinia } from "pinia";
import router from "./router";
import App from "./App.vue";

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

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



// app.use(EdaVue);
app.use(pinia);
app.use(router);
app.mount("#app");

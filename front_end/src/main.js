import { createApp } from "vue"

import App from "./App.vue"
import VueCookies from "vue-cookies"
import router from "@/tools/index.js"
import store from "@/tools/store.js"
import BootstrapVue3 from "bootstrap-vue-3"
import i18n from './i18n'

import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue-3/dist/bootstrap-vue-3.css"

const app = createApp(App);

router.beforeEach((to, from, next) => {
    i18n.locale = window.$cookies.get("lang");
    next();
});

app.component(VueCookies);

app.use(store);
app.use(router);
app.use(BootstrapVue3);
app.use(i18n);

app.mount("#app");

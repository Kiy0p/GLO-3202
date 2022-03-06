import { createApp } from "vue"
import { createStore } from 'vuex'
import App from "./App.vue"
import VueCookies from "vue-cookies"
import router from "@/router/index.js"
import createPersistedState from "vuex-persistedstate";


export const store = createStore({
    state: {
        authenticated: false,
        token: localStorage.getItem("notes_token")
    },
    mutations: {
        setAuthentication(state, status) {
            state.authenticated = status;
        }
    },
    plugins: [createPersistedState()],
});

const app = createApp(App);

app.component(VueCookies);

app.use(store);
app.use(router);

app.mount("#app");

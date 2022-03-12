import Login from "@/components/LoginView.vue"
import Home from "@/components/HomeView.vue"
import Register from "@/components/RegisterView.vue"
import NotFound from "@/components/NotFound.vue"
import store from "@/tools/store.js"
import { createRouter, createWebHashHistory } from "vue-router"


// Application routes

const routes = [
    { path: "/signin", name: "signin", component: Login },
    { path: "/signup", name: "signup", component: Register },
    {
        path: "/",
        name: "home",
        component: Home,
        beforeEnter: (to, from, next) => {
            if (store.state.authenticated == false) {
                next({ name: 'signin' });
            } else {
                next();
            }
        }
    },
    { path: "/:pathMatch(.*)*", name: "notFound", component: NotFound },
]

// Create router and feed routes

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})

export default router;
import SignIn from "@/views/SignIn.vue"
import SignUp from "@/views/SignUp.vue"
import Home from "@/views/HomeView.vue"
import NotFound from "@/views/NotFound.vue"
import store from "@/tools/store.js"
import { createRouter, createWebHashHistory } from "vue-router"


// Application routes

const routes = [
    { path: "/signin", name: "signin", component: SignIn },
    { path: "/signup", name: "signup", component: SignUp },
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
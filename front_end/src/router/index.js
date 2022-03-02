import Login from "@/components/LoginView.vue"
import Home from "@/components/HomeView.vue"
import Register from "@/components/RegisterView.vue"
import { createRouter, createWebHashHistory } from "vue-router"


// Application routes

const routes = [
    { path: "/login", component: Login },
    { path: "/register", component: Register },
    { path: "/", component: Home },
]

// Create router and feed routes

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})

export default router;
import createPersistedState from "vuex-persistedstate"
import { createStore } from "vuex"

const store = createStore({
    state: {
        authenticated: false,
        token: window.$cookies.get("notes_token")
    },
    mutations: {
        setAuthentication(state, status) {
            state.authenticated = status;
        }
    },
    plugins: [createPersistedState()],
});

export default store
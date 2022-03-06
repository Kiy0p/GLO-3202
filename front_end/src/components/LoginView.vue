<template>
  <div>
    <h1>Login</h1>
    <div id="form-container">
      <form id="login-form">
        <input
          class="input"
          type="text"
          v-model="username"
          placeholder="username"
        />
        <input
          class="input"
          type="password"
          v-model="password"
          placeholder="password"
        />
        <input
          class="input"
          type="button"
          value="Login"
          v-on:click="postSignIn"
        />
      </form>
    </div>
    <p>Don't have an account yet ?</p>
    <router-link to="/signup">Register</router-link>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginView",

  data() {
    return {
      username: "",
      password: "",
    };
  },

  methods: {
    async postSignIn() {
      await axios({
        method: "POST",
        url: "http://localhost:8000/api/sign/in",
        data: { username: this.username, password: this.password },
      })
        .then((response) => {
          localStorage.setItem("notes_token", response.data["token"]);
          this.$store.commit("setAuthentication", true);
          this.$router.replace({ name: "home" });
        })
        .catch((error) => {
          if (error.response.status == 401)
            window.alert("Invalid username or password.");
          else window.alert(error.response.data.error[0]);
        });
    },
  },
};
</script>

<style scoped>
#form-container {
  display: flex;
  justify-content: center;
}

#login-form {
  display: flex;
  flex-direction: column;
  width: 25%;
}

.input {
  margin-top: 1em;
}
</style>

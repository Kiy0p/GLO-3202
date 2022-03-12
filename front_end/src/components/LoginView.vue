<template>
  <div>
    <h1>Login</h1>
    <div id="form-container">
      <b-form id="login-form" @submit="postSignIn">
        <b-form-input
          id="input-username"
          class="input"
          v-model="username"
          type="text"
          placeholder="Enter username"
          size="lg"
          required
          autofocus
        ></b-form-input>
        <b-form-input
          id="input-password"
          class="input"
          v-model="password"
          type="password"
          placeholder="Enter password"
          size="lg"
          required
        ></b-form-input>
        <b-button
          class="input"
          variant="outline-primary"
          size="lg"
          type="submit"
          >Login
        </b-button>
      </b-form>
    </div>
    <div id="router-container">
      <p>Don't have an account yet ?</p>
      <router-link to="/signup">Register</router-link>
    </div>
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
  width: 40%;
}

#router-container {
  padding: 3em;
  font-family: "RobotoRegular";
}

.input {
  margin-top: 1em;
}
</style>

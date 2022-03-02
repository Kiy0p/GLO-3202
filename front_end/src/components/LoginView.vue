<template>
  <div>
    <h1>Login</h1>
    <div id="form-container">
      <form method="post" action="" id="login-form">
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
          v-on:click="submitLogin"
        />
      </form>
    </div>
    <p>Don't have an account yet ?</p>
    <router-link to="/register">Register</router-link>
  </div>
</template>

<script>
export default {
  name: "LoginView",

  data() {
    return {
      username: "",
      password: "",
    };
  },

  methods: {
    submitLogin: function () {
      this.$router.push("/");
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

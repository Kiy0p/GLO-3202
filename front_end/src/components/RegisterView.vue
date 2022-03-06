<template>
  <div>
    <h1>Register</h1>
    <div id="form-container">
      <form method="post" action="" id="register-form">
        <input class="input" type="email" v-model="email" placeholder="email" />
        <input
          class="input"
          type="text"
          v-model="username"
          placeholder="username"
        />
        <input
          class="input"
          type="password"
          v-model="pass1"
          placeholder="password"
        />
        <input
          class="input"
          type="password"
          v-model="pass2"
          placeholder="repeat password"
        />
        <input
          class="input"
          type="button"
          value="Register"
          v-on:click="postSignUp"
        />
      </form>
    </div>
    <p>Back to login</p>
    <router-link to="/signin">Login</router-link>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterView",
  data() {
    return {
      email: "",
      username: "",
      pass1: "",
      pass2: "",
    };
  },
  methods: {
    async postSignUp() {
      if (this.isFormValid() !== "") {
        window.alert(this.isFormValid());
        return;
      }
      await axios({
        method: "POST",
        url: "http://localhost:8000/api/sign/up",
        data: {
          username: this.username,
          email: this.email,
          password: this.pass1,
        },
      })
        .then(() => {
          this.$router.push("/signin");
        })
        .catch((error) => {
          if (error.response.status == 400)
            window.alert("email or username is allready taken.");
          if (error.response.status == 401)
            window.alert(error.response.data.error[0]);
        });
    },

    isFormValid() {
      if (this.pass1 !== this.pass2) return "Passwords don't match.";
      if (!this.pass1.match(/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$/))
        return "Password must contain at least 8 characters, capital letters, lower case letters and digits.";
      if (this.username.length < 5)
        return "Username must be at least 5 characters long.";
      if (
        !this.email.match(
          /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
        )
      )
        return "Incorrect email.";
      return "";
    },
  },
};
</script>

<style scoped>
#form-container {
  display: flex;
  justify-content: center;
}

#register-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 25%;
}

.input {
  margin-top: 1em;
}
</style>
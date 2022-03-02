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
          v-on:click="submitRegister"
        />
      </form>
    </div>
    <p>Back to login</p>
    <router-link to="/login">Login</router-link>
  </div>
</template>

<script>
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
  mathods: {
    submitRegister: function () {
      console.log("submitted form");
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
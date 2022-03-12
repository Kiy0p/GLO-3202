<template>
  <div>
    <h1>Register</h1>
    <div id="form-container">
      <b-form id="register-form" @submit="postSignUp">
        <b-form-group>
          <b-form-input
            id="input-email"
            class="input"
            v-model="email"
            type="email"
            placeholder="Enter email"
            size="lg"
            required
            autofocus
            :state="emailCorrect"
          ></b-form-input>
          <b-form-invalid-feedback :state="emailCorrect">
            Enter a valid email.
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group>
          <b-form-input
            id="input-username"
            class="input"
            v-model="username"
            type="text"
            placeholder="Enter username"
            size="lg"
            required
            :state="usernameLength"
          ></b-form-input>
          <b-form-invalid-feedback :state="usernameLength">
            Username sould at least be 5 characters long.
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group>
          <b-form-input
            id="input-pass1"
            class="input"
            v-model="pass1"
            type="password"
            placeholder="Enter password"
            size="lg"
            required
            :state="passwordRequirements"
          ></b-form-input>
          <b-form-invalid-feedback :state="passwordRequirements">
            Password should at least contain 8 characters, uppercase, lowercase
            and numbers.
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group>
          <b-form-input
            id="input-pass2"
            class="input"
            v-model="pass2"
            type="password"
            placeholder="Reprat password"
            size="lg"
            required
            :state="passwordsMatch"
          ></b-form-input>
          <b-form-invalid-feedback :state="passwordsMatch">
            Passwords don't match.
          </b-form-invalid-feedback>
        </b-form-group>
        <b-button
          class="input"
          variant="outline-primary"
          size="lg"
          type="submit"
          >Register
        </b-button>
      </b-form>
    </div>
    <div id="router-container">
      <p>Back to login</p>
      <router-link to="/signin">Login</router-link>
    </div>
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
      emailContext: null,
      usernameContext: null,
      pass1Context: null,
      pass2Context: null,
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
  },
  computed: {
    emailCorrect() {
      if (this.email === "") return null;
      if (
        !this.email.match(
          /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
        )
      )
        return false;
      return true;
    },

    usernameLength() {
      if (this.username === "") return null;
      if (this.username.length < 5) return false;
      return true;
    },

    passwordRequirements() {
      if (this.pass1 === "") return null;
      if (!this.pass1.match(/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$/))
        return false;
      return true;
    },

    passwordsMatch() {
      if (this.pass2 === "") return null;
      if (this.pass1 !== this.pass2) return false;
      return true;
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
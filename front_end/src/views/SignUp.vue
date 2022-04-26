<template>
  <div>
    <Alert variant="danger" ref="alertComponent" />
    <h1 id="form-title">{{ $t("register.title", language) }}</h1>
    <div id="form-container">
      <b-form id="register-form" class="w-75" @submit="postSignUp">
        <b-form-group class="form-group">
          <b-form-input
            id="input-email"
            class="input"
            v-model="email"
            type="email"
            :placeholder="$t('register.formEmail', language)"
            size="lg"
            required
            autofocus
            :state="emailCorrect"
          ></b-form-input>
          <b-form-invalid-feedback :state="emailCorrect">
            {{ $t("register.feedBack.email", language) }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group class="form-group">
          <b-form-input
            id="input-username"
            class="input"
            v-model="username"
            type="text"
            :placeholder="$t('register.formUsername', language)"
            size="lg"
            required
            :state="usernameLength"
          ></b-form-input>
          <b-form-invalid-feedback :state="usernameLength">
            {{ $t("register.feedBack.username", language) }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group class="form-group">
          <b-form-input
            id="input-pass1"
            class="input"
            v-model="pass1"
            type="password"
            :placeholder="$t('register.formpassword1', language)"
            size="lg"
            required
            :state="passwordRequirements"
          ></b-form-input>
          <b-form-invalid-feedback :state="passwordRequirements">
            {{ $t("register.feedBack.password1", language) }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group class="form-group">
          <b-form-input
            id="input-pass2"
            class="input"
            v-model="pass2"
            type="password"
            :placeholder="$t('register.formpassword2', language)"
            size="lg"
            required
            :state="passwordsMatch"
          ></b-form-input>
          <b-form-invalid-feedback :state="passwordsMatch">
            {{ $t("register.feedBack.password2", language) }}
          </b-form-invalid-feedback>
        </b-form-group>
        <b-button
          class="input"
          variant="outline-primary"
          size="lg"
          type="submit"
          >{{ $t("register.formButton", language) }}
        </b-button>
      </b-form>
    </div>
    <div id="router-container">
      <p>{{ $t("register.formFooter", language) }}</p>
      <router-link to="/signin">{{
        $t("register.formLogin", language)
      }}</router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "@/components/Alert";

export default {
  name: "RegisterView",

  components: {
    Alert,
  },

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
      language: "en",
    };
  },
  methods: {
    async postSignUp() {
      await axios({
        method: "POST",
        url: process.env.VUE_APP_ROOT_API + "/api/sign/up",
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
            this.$refs.alertComponent.showAlert(
              this.$t("register.alert.emailTaken", this.language)
            );
          else if (error.response.status == 401)
            this.$refs.alertComponent.showAlert(
              this.$t("register.alert.unnothorized", this.language)
            );
          else
            this.$refs.alertComponent.showAlert(
              this.$t("register.alert.somethingWentWrong", this.language)
            );
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
  mounted() {
    this.language = window.$cookies.get("lang");
  },
};
</script>

<style scoped>
@import "@/styles/views/signup.css";
@import "@/styles/views/commonSign.css";
</style>
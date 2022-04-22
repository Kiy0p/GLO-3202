<template>
  <div>
    <Alert
      variant="danger"
      content="Invalid username or password."
      ref="alertComponent"
    />
    <h1 id="form-title">{{ $t("login.title", language) }}</h1>
    <div id="form-container">
      <b-form id="login-form" class="w-75" @submit="postSignIn">
        <b-form-group class="form-group">
          <b-form-input
            id="input-username"
            class="input"
            v-model="username"
            type="text"
            :placeholder="$t('login.formUsername', language)"
            size="lg"
            required
            autofocus
          ></b-form-input>
        </b-form-group>
        <b-form-group class="form-group">
          <b-form-input
            id="input-password"
            class="input"
            v-model="password"
            type="password"
            :placeholder="$t('login.formPassword', language)"
            size="lg"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group class="form-group">
          <b-button
            id="login-button"
            class="input"
            variant="outline-primary"
            size="lg"
            type="submit"
            >{{ $t("login.formButton", language) }}
          </b-button>
        </b-form-group>
      </b-form>
    </div>
    <div id="router-container">
      <p>{{ $t("login.formFooter", language) }}</p>
      <router-link to="/signup">{{ $t("login.formRegister", language) }}</router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "@/components/Alert";

export default {
  name: "LoginView",

  components: {
    Alert,
  },

  data() {
    return {
      username: "",
      password: "",
      language: "en",
    };
  },

  methods: {
    async postSignIn() {
      await axios({
        method: "POST",
        url: process.env.VUE_APP_ROOT_API + "/api/sign/in",
        data: { username: this.username, password: this.password },
      })
      .then((response) => {
        window.$cookies.set("notes_token", response.data["token"]);
        this.$store.commit("setAuthentication", true);
        this.$router.replace({ name: "home" });
      })
      .catch((error) => {
        if (error.response.status == 401) {
          this.$refs.alertComponent.showAlert();
        }
        else window.alert(error.response.data.error[0]);
      });
    },
  },
  mounted() {
    this.language = window.$cookies.get("lang");
  },
};
</script>

<style scoped>
@import "@/styles/signin.css";
@import "@/styles/commonSign.css";
</style>

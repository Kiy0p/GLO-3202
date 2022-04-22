<template>
  <div>
    <h1 id="title">{{ $t("home.title", language) }}</h1>
    <div id="form-container">
      <b-form id="form" @submit="createNote()">
        <b-form-input
          id="noteTitleInput"
          class="form-input"
          v-model="noteTitle"
          :placeholder="$t('home.formTitle', language)"
          size="lg"
        >
        </b-form-input>
        <b-form-textarea
          id="noteContentInput"
          class="form-input"
          v-model="noteContent"
          :placeholder="$t('home.formContent', language)"
          size="lg"
          rows="3"
          no-resize
        >
        </b-form-textarea>
        <b-button
          id="form-button-create"
          class="form-input"
          variant="outline-primary"
          type="submit"
          size="lg"
        >{{ $t("home.formButton", language) }}</b-button>
      </b-form>
      <hr size="4" width="90%" color="2c3e50" />
    </div>
    <div class="notes-container">
      <Note
        v-for="(note, index) in notes"
        :key="index"
        :title="note.title"
        :content="note.content"
        :id="note.id"
        :token="token"
        @noteDeleted="getNotes()"
      />
    </div>
    <div v-if="notes == []">
      <p>No Posts to show.</p>
    </div>
    <div id="router-container">
      <p>{{ $t("home.formFooter", language) }}</p>
      <router-link to="/signin" v-on:click="logout()">{{ $t("home.formLogout", language) }}</router-link>
    </div>
  </div>
</template>

<script>
import Note from "@/components/NoteView.vue";

import axios from "axios";
export default {
  name: "HomeView",

  data() {
    return {
      notes: [],
      token: null,
      noteTitle: "",
      noteContent: "",
      language: "en",
    };
  },

  components: {
    Note,
  },

  methods: {
    async getNotes() {
      await axios({
        method: "post",
        url: process.env.VUE_APP_ROOT_API + "/api/notes/", // 20.199.116.68:80/api/notes/
        headers: {
          Authorization: `Token ${this.token}`,
          "Content-Type": "application/json",
        },
      })
      .then((response) => {
        if (response.status == 200) {
          this.notes = response.data;
        } else {
          this.$router.replace({ name: "signin" });
        }
      })
      .catch(() => {
        this.$router.replace({ name: "signin" });
      });
    },

    async createNote() {
      await axios({
        method: "post",
        url: process.env.VUE_APP_ROOT_API + "/api/notes/create/", // 20.199.116.68:80/api/notes/create/
        headers: {
          Authorization: `Token ${this.token}`,
          "Content-Type": "application/json",
        },
        data: {
          note_title: this.noteTitle,
          note_content: this.noteContent,
        },
      })
        .then((response) => {
          if (response.status == 201) {
            this.getNotes();
            this.clearInputs();
          } else {
            window.alert(
              "Note couldn't be created, status:" + response.statusText
            );
          }
        })
        .catch(() => {
          this.$router.replace({ name: "signin" });
        });
    },
    clearInputs() {
      this.noteTitle = "";
      this.noteContent = "";
    },
    logout() {
      window.$cookies.remove("notes_token");
      this.$store.commit("setAuthentication", false);
    },
  },

  async mounted() {
    this.token = window.$cookies.get("notes_token");
    this.language = window.$cookies.get("lang");
    await this.getNotes();
  },
};
</script>

<style scoped>
@import "@/styles/home.css";
</style>

<template>
  <div>
    <h1 id="title"></h1>
    <div id="form-container">
      <b-form id="form" @submit="createNote()">
        <b-form-input
          id="noteTitleInput"
          class="form-input"
          v-model="noteTitle"
          placeholder="Title"
          size="lg"
        >
        </b-form-input>
        <b-form-textarea
          id="noteContentInput"
          class="form-input"
          v-model="noteContent"
          placeholder="Content"
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
        ></b-button>
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
      <p>Back to login</p>
      <router-link to="/signin" v-on:click="logout()">Log out</router-link>
    </div>
  </div>
</template>

<script>
import Note from "./NoteView.vue";
import { language } from "@/lang/lang.js";

import axios from "axios";
export default {
  name: "HomeView",

  data() {
    return {
      notes: [],
      token: null,
      noteTitle: "",
      noteContent: "",
    };
  },

  components: {
    Note,
  },

  methods: {
    async getNotes() {
      await axios({
        method: "post",
        url: "http://localhost:8000/api/notes/", // 20.199.116.68:80/api/notes/
        headers: {
          Authorization: `Token ${this.token}`,
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          this.notes = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    async createNote() {
      if (!this.checkForm()) return;
      await axios({
        method: "post",
        url: "http://localhost:8000/api/notes/create/", // 20.199.116.68:80/api/notes/create/
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
        .catch((error) => {
          console.log(error);
          window.alert(error);
        });
    },

    checkForm() {
      if (this.noteTitle === "" || this.noteContent === "") return false;
      return true;
    },

    clearInputs() {
      this.noteTitle = "";
      this.noteContent = "";
    },

    loadLanguage() {
      // loads the language with the cookie lang
      if (window.$cookies.get("lang")) {
        // if cookie is set
        const title = document.getElementById("title");
        const button = document.getElementById("form-button-create");
        const inputTitle = document.getElementById("noteTitleInput");
        const inputContent = document.getElementById("noteContentInput");
        if (window.$cookies.get("lang") == "fr") {
          title.textContent = language.fr.title;
          button.textContent = language.fr.formButton;
          inputTitle.setAttribute("placeholder", language.fr.formTitle);
          inputContent.setAttribute("placeholder", language.fr.formContent);
        } else if (window.$cookies.get("lang") == "en") {
          title.textContent = language.en.title;
          button.textContent = language.en.formButton;
          inputTitle.setAttribute("placeholder", language.en.formTitle);
          inputContent.setAttribute("placeholder", language.en.formContent);
        } else {
          // if cookie doesn't match any language, sets it to default.
          window.$cookies.set("lang", "en", Infinity);
          this.loadLanguage();
        }
      } else {
        // if cookie is not set, sets it and reloads the page
        window.$cookies.set("lang", "en", Infinity);
        this.loadLanguage();
      }
    },
    logout() {
      localStorage.removeItem("notes_token");
      this.$store.commit("setAuthentication", false);
    },
  },

  async mounted() {
    this.token = localStorage.getItem("notes_token");
    await this.getNotes();
    this.loadLanguage();
  },
};
</script>

<style scoped>
.notes-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
}

.form-input {
  margin-top: 1em;
}

#title {
  font-size: 8em;
  font-family: "RobotoRegular", Helvetica, Arial;
}

#form {
  display: flex;
  flex-direction: column;
  width: 30%;
  margin-bottom: 20px;
  align-items: center;
}

#form-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-bottom: 40px;
}

#form-button-create {
  font-family: "RobotoBold";
  width: 5em;
}

#noteTitleInput {
  font-family: "MonospaceBold";
}

#noteContentInput {
  font-family: "MonospaceBold";
}

#router-container {
  padding: 3em;
  font-family: "RobotoRegular";
}
</style>

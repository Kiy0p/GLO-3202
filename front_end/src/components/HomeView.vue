<template>
  <div>
    <div id="flag-container">
      <input
        type="image"
        class="flag"
        v-on:click="changeLanguage('fr')"
        :src="require('@/assets/french_flag.png')"
      />
      <input
        type="image"
        class="flag"
        v-on:click="changeLanguage('en')"
        :src="require('@/assets/english_flag.png')"
      />
    </div>
    <h1 id="title"></h1>
    <div id="form-container">
      <form id="form">
        <input id="form-title" type="text" autocomplete="off" />
        <textarea id="form-content"></textarea>
        <input
          id="form-submit"
          type="submit"
          value="Create"
          v-on:click="createNote()"
        />
      </form>
      <hr size="4" width="90%" color="2c3e50" />
    </div>
    <div class="notes-container">
      <Note
        v-for="(note, index) in notes"
        :key="index"
        :v-if="notes == []"
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
    <p>Back to login</p>
    <router-link to="/signin" v-on:click="logout()">Log out</router-link>
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
      var title = document.getElementById("form-title").value;
      var content = document.getElementById("form-content").value;
      await axios({
        method: "post",
        url: "http://localhost:8000/api/notes/create/", // 20.199.116.68:80/api/notes/create/
        headers: {
          Authorization: `Token ${this.token}`,
          "Content-Type": "application/json",
        },
        data: {
          note_title: title,
          note_content: content,
        },
      })
        .then((response) => {
          if (response.status == 201) {
            this.getNotes();
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

    changeLanguage(language) {
      window.$cookies.set("lang", language, Infinity);
      location.reload();
    },

    loadLanguage() {
      // loads the language with the cookie lang
      if (window.$cookies.get("lang")) {
        // if cookie is set
        var title = document.getElementById("title");
        if (window.$cookies.get("lang") == "fr") {
          title.textContent = language.fr.title;
        } else if (window.$cookies.get("lang") == "en") {
          title.textContent = language.en.title;
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
#flag-container {
  display: flex;
  flex-direction: row;
  margin-top: 20px;
  margin-right: 20px;
  margin-left: 20px;
}

.flag {
  width: 60px;
  height: 40px;
  margin-right: 20px;
}

.notes-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
}

#title {
  font-size: 8em;
}

#form {
  display: flex;
  flex-direction: column;
  width: 24%;
  margin-bottom: 20px;
}

#form-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-bottom: 40px;
}

#form-title {
  color: blue;
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 20px;
}

#form-content {
  font-size: 20px;
  margin-bottom: 20px;
}

#form-submit {
  font-size: 20px;
  width: 100px;
  align-self: center;
}
</style>

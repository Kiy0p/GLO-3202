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
    <div id="title-container">
      <h2 id="userId"></h2>
      <h2>{{ userId }}</h2>
    </div>
    <div id="form-container">
      <form id="form">
        <input id="form-title" type="text" autocomplete="off" />
        <textarea id="form-content"></textarea>
        <input
          id="form-submit"
          type="submit"
          value="Create"
          v-on:click="createNote"
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
        :userId="userId"
        @noteDeleted="getNotes()"
      />
    </div>

    <div v-if="notes == []">
      <p>No Posts to show.</p>
    </div>
  </div>
</template>

<script>
import Note from "./Note.vue";
import { uuid } from "vue-uuid";
import { language } from "@/lang/lang.js";

import axios from "axios";
export default {
  name: "Home",

  data() {
    return {
      notes: [],
      userId: null,
    };
  },

  components: {
    Note,
  },

  methods: {
    async getNotes() {
      console.log("reloading");
      await axios({
        method: "post",
        url: "http://127.0.0.1:8000/notes/",
        data: { user_id: this.userId },
      }).then((response) => {
        this.notes = response.data;
      });
    },

    async createNote() {
      var title = document.getElementById("form-title").value;
      var content = document.getElementById("form-content").value;
      await axios({
        method: "post",
        url: "http://127.0.0.1:8000/notes/create/",
        data: {
          user_id: this.userId,
          note_title: title,
          note_content: content,
        },
      }).then((response) => {
        if (response.statusCode == 200) {
          this.getNotes();
        }
      });
    },

    createUUID() {
      if (localStorage.getItem("notes_user_id") == null) {
        var userUUID = uuid.v1();
        localStorage.setItem("notes_user_id", userUUID);
      }
      this.userId = localStorage.getItem("notes_user_id");
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
        var userId = document.getElementById("userId");
        if (window.$cookies.get("lang") == "fr") {
          title.textContent = language.fr.title;
          userId.textContent = language.fr.userId;
        } else if (window.$cookies.get("lang") == "en") {
          title.textContent = language.en.title;
          userId.textContent = language.en.userId;
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
  },

  async mounted() {
    this.createUUID();
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
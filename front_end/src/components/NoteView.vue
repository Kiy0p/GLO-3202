<template>
  <b-card class="post-container" bg-variant="light" :header="title">
    <b-card-text class="post-content">
      {{ content }}
    </b-card-text>
    <b-button
      id="button-delete"
      type="submit"
      variant="outline-danger"
      @click="deletePost"
      >{{ buttonText }}
    </b-button>
  </b-card>
</template>

<script>
import axios from "axios";
import { language } from "@/lang/lang.js";

export default {
  name: "NoteView",

  props: ["title", "content", "id", "token"],

  data() {
    return {
      buttonText: "",
    };
  },

  methods: {
    deletePost() {
      axios({
        method: "delete",
        url: "http://localhost:8000/api/notes/delete/", // 20.199.116.68:80/api/notes/delete
        headers: {
          Authorization: `Token ${this.token}`,
          "Content-Type": "application/json",
        },
        data: { note_id: this.id },
      })
        .then(() => {
          this.$emit("noteDeleted");
        })
        .catch((error) => {
          console.log(error);
          window.alert(error);
        });
    },

    loadLanguage() {
      // if cookie is set
      if (window.$cookies.get("lang") == "fr") {
        this.buttonText = language.fr.noteButton;
      } else if (window.$cookies.get("lang") == "en") {
        this.buttonText = language.en.noteButton;
      } else {
        this.buttonText = language.en.noteButton;
      }
    },
  },

  mounted() {
    this.loadLanguage();
  },
};
</script>

<style scoped>
.post-container {
  width: 24%;
  margin-bottom: 18px;
  word-wrap: break-word;
  font-family: "MonospaceBold";
  font-size: 30px;
  display: flex;
}

.post-items-container {
  flex-direction: column;
  justify-content: space-between;
}

.post {
  display: flex;
  flex-direction: column;
  margin: auto;
  overflow: auto;
}

.post-content {
  font-family: "MonospaceBold";
  font-size: 20px;
}

#button-delete {
  font-family: "RobotoBold";
}
</style>

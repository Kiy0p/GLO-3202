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
      >{{ $t("note.deleteButton", language) }}
    </b-button>
  </b-card>
</template>

<script>
import axios from "axios";

export default {
  name: "NoteView",

  props: ["title", "content", "id", "token"],

  data() {
    return {
      buttonText: "",
      language: "en",
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
        .catch(() => {
          this.$router.replace({ name: "signin" });
        });
    },
  },

  mounted() {
    this.language = window.$cookies.get("lang");
  },
};
</script>

<style scoped>
@import "@/styles/note.css";
</style>

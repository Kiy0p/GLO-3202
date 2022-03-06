<template>
  <div class="post-container" v-if="isActive">
    <div class="post">
      <div class="post-title">{{ title }}</div>
      <div class="post-content">{{ content }}</div>
    </div>
    <button type="submit" class="delete-button" @click="deletePost">X</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "NoteView",
  props: ["title", "content", "id", "token"],
  data() {
    return {
      isActive: true,
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
  },
};
</script>

<style scoped>
.post-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border: 1px solid black;
  width: 24%;
  margin-bottom: 18px;
  word-wrap: break-word;
}

.post {
  display: flex;
  flex-direction: column;
  margin: auto;
  overflow: auto;
}

.post-title {
  color: blue;
  font-size: 30px;
  font-weight: bold;
}

.post-content {
  font-size: 20px;
}

.delete-button {
  align-self: right;
  background-color: red;
  font-size: 15px;
  color: white;
  height: 20px;
  width: 20px;
  flex: none;
}
</style>

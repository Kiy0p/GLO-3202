<template>
  <div id="alert-container" class="w-100">
    <b-alert
      class="mx-auto my-auto alert"
      :show="isActive"
      fade
      :variant="variant"
      >{{ content }}</b-alert
    >
  </div>
</template>

<script>
export default {
  name: "AlertComponent",

  props: ["variant"],

  data() {
    return {
      isActive: false,
      content: "Something went wrong, try again later",
    };
  },

  methods: {
    showAlert(value) {
      this.isActive = true;
      this.content = value;
      setTimeout(() => {
        this.isActive = false;
      }, 4000);
    },
  },
};
</script>

<style scoped>
@import "@/styles/components/alert.css";
</style>
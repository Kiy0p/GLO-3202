<template>
  <div id="alert-container" class="w-100">
    <b-alert class="mx-auto my-auto" :show="isActive" fade :variant="variant">{{ content }}</b-alert>
  </div>
</template>

<script>
export default {
  name: "AlertView",

  props: ["variant", "content"],

  data() {
    return {
      isActive: false,
    }
  },

  methods: {
    showAlert() {
      this.isActive = true;
      setTimeout(() => { this.isActive = false }, 3000);
    },
  }

}
</script>

<style scoped>
#alert-container {
  display: flex;
  position: absolute;
  margin-top: -85px;
}
</style>
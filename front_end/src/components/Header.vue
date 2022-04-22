<template>
  <header id="flag-container">
    <div>
      <input
        type="image"
        class="flag"
        v-on:click="changeLanguage('fr')"
        :src="require('@/assets/images/french_flag.png')"
      />
      <input
        type="image"
        class="flag"
        v-on:click="changeLanguage('en')"
        :src="require('@/assets/images/english_flag.png')"
      />
    </div>
    <h1 id="site-title">Notes.io</h1>
  </header>
</template>

<script>
export default {
  name: "headerView",
  methods: {
    changeLanguage(language) {
      window.$cookies.set("lang", language, Infinity);
      location.reload();
    },
  },
};
</script>


<style scoped>
@import "@/styles/components/header.css";
</style>
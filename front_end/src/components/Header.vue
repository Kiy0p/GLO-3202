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
      console.log("reloading");
    },
  },
};
</script>


<style scoped>
.flag {
  width: 60px;
  height: 40px;
  margin-right: 20px;
}

#flag-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 20px;
  margin-right: 20px;
  margin-left: 20px;
}

#site-title {
  font-family: "RobotoBold";
  align-self: center;
  font-size: 3em;
}
</style>
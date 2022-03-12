<template>
  <div>
    <Lang />
    <router-view />
  </div>
</template>

<script>
import Lang from "@/components/Header.vue";

export default {
  name: "App",
  components: {
    Lang,
  },
};
</script>

<style>
#app {
  font-family: Times, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

* {
  margin: 0;
  padding: 0;
}

@font-face {
  font-family: "RobotoRegular";
  src: local("Roboto"),
    url(./assets/fonts/Roboto/Roboto-Regular.ttf) format("truetype");
}

@font-face {
  font-family: "RobotoBold";
  src: local("Roboto"),
    url(./assets/fonts/Roboto/Roboto-Bold.ttf) format("truetype");
}

@font-face {
  font-family: "MonospaceBold";
  src: local("Monospace"),
    url(./assets/fonts/Monospace/Monospace-Bold.ttf) format("truetype");
}
</style>

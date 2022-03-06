<template>
  <div>
    <h1>404 Not found</h1>
    <p>The URL must be incorrect...</p>
    <p>Back to login</p>
    <router-link to="/signin">Log in</router-link>
  </div>
</template>

<script>
export default {
  name: "NotFoundView",

  data() {
    return {};
  },
};
</script>

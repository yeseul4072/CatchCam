<template>
  <v-app>
    <Header />
    <v-main class="page">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Header from "@/components/Header";
export default {
  name: "App",
  components: {
    Header,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style scoped>
.page {
  background-color: black;
  color: white;
}
</style>
<template>
  <div class="header d-flex justify-space-between">
    <div>
      <v-img
      class="logo ma-3"
      src="@/assets/logo2.png"
      @click="$router.push({name: 'Home'})"
      ></v-img>
    </div>
    <div>
      <v-btn
      class="ma-5"
      color="#ffffff"
      dark
      rounded
      large
      outlined
      @click="$router.push({name: 'Login'})"
      >로그인하고 대여하기</v-btn>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.logo {
  width: 200px;
  cursor: pointer;
}
.header {
  position: fixed;
  z-index: 8000;
  width: 100%;
}
</style>
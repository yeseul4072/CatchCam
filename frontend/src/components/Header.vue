<template>
  <div class="header d-flex justify-space-between">
      <h2>CatchCam</h2>
      <v-btn
  elevation="2"
  outlined
  rounded
  dark
  @click="$router.push({name: 'Login'})"
>로그인하고 대여하기</v-btn>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.header {
  position: fixed;
  z-index: 8000;
  color: white;
  width: 100%;
}
</style>
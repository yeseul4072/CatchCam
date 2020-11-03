<template>
  <v-container class="dronespec">
    <v-row>
      <v-col offset="2" cols="4">
        <v-img :src="drone.image"></v-img>
      </v-col>
      <v-col offset="1" cols="4">
        <h1>드론스펙</h1>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "DroneSpec",
  data() {
    return {
      drone: {
        name: "캐치캠 v1.0",
        description:
          "드론은 본래 군사용으로 개발되어 점차 그 기술이 발전함에 따라 무궁무진한 가능성을 품고 있는 4차 산업혁명의 신산업 분야라고 말할 수 있습니다. 최초의 형태는 열기구로 1849년에 오스트리아의 전투에서 실제로 사용되었고 뒤이어 제 1,2차 세계대전에서 중요한 전투무기로 사용되기도 하였습니다.",
        image: require("@/assets/drone3.png"),
        charge: 10000,
      },
    };
  },
};
</script>

<style scoped>
.dronespec {
  margin-top: 10vh;
}
</style>
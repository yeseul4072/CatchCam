<template>
  <v-container class="droneintro">
    <v-row>
      <v-col cols="8">
        <div class="text-h4 title">{{ drone.name }}</div>
        <div class="text-h5">{{ drone.cost }}원 / 일</div>
        <v-img :src="drone.image"></v-img>
          <v-tabs 
            fixed-tabs
            background-color="transparent"
            color="#018F26"
          >
            <v-tab style="color:white">상품 설명</v-tab>
            <v-tab style="color:white">대여 이용 안내</v-tab>
            <v-tab style="color:white">후기</v-tab>
            <v-tab style="color:white">질문</v-tab>
          </v-tabs>
        <div class="subtitle">상품 설명</div>
        <div>{{ drone.description }}</div>

        <div class="subtitle">사용 방법</div>
        <div class="subtitle">이용 안내</div>
        <div class="subtitle">후기</div>
        <Reviews :droneId="drone_id"/>
        <div class="subtitle">질문</div>
        
      </v-col>
      <v-col class="pl-10" cols="4">
        <Rental :drone="drone"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import axios from 'axios'
import Rental from '@/components/droneintro/Rental'
import Reviews from '@/components/droneintro/Reviews'


export default {
  name: "DroneIntro",
  components: {
    Rental,
    Reviews,
  },
  data() {
    return {
      drone: {
        id: 0,
        name: "캐치캠 v1.0",
        description:
          "드론은 본래 군사용으로 개발되어 점차 그 기술이 발전함에 따라 무궁무진한 가능성을 품고 있는 4차 산업혁명의 신산업 분야라고 말할 수 있습니다. 최초의 형태는 열기구로 1849년에 오스트리아의 전투에서 실제로 사용되었고 뒤이어 제 1,2차 세계대전에서 중요한 전투무기로 사용되기도 하였습니다.",
        image: require("@/assets/drone4.png"),
        cost: 50000,
      },
    };
  },
  // created () {
  //   axios.get('') 
  //   .then (res => {

  //   })
  //   .catch (res => {

  //   })
  // }
};
</script>

<style scoped>
.droneintro {
  margin-top: 5vh;
}
.title {
  font-weight: 900;
  height: 50px;
  margin-top: 10vh;
}
.subtitle {
  margin-top: 10vh;
  margin-bottom: 2vh;
  font-size: 25px;
  font-weight: bold;
}
.map_wrap {
  width: 1%;
}
</style>
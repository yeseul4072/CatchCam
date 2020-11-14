<template>
  <v-container class="droneintro">
    <v-row>
      <v-col cols="8">
        <div class="text-h4 title">{{ drone.itemName }}</div>
        <div class="text-h5">{{ drone.cost | comma }}원 / 일</div>
        <v-img src="@/assets/drone4.png"></v-img>
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
        <v-img
          class="mx-15"
          src="@/assets/guide.png"
        ></v-img>
        <div class="subtitle">후기</div>
        <Reviews :drone="drone"/>
        <!-- <div class="subtitle">질문</div> -->
        
      </v-col>
      <v-col class="pl-10" cols="4">
        <Rental :drone="drone"/>
      </v-col>
    </v-row>
    <Footer/>
  </v-container>
</template>

<script>
// import axios from 'axios'
import Rental from '@/components/droneintro/Rental'
import Reviews from '@/components/droneintro/Reviews'
import Footer from '@/components/Footer'
import http from '@/api/api.js'


export default {
  name: "DroneIntro",
  components: {
    Rental,
    Reviews,
    Footer
  },
  data() {
    return {
      drone: null,
      rentalTop: 0,
    };
  },
  filters: {
    comma: function(value) {
      var num = new Number(value);
      return num.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
    }
  },
  created () {
    http.axios.get('/item/1') 
    .then (res => {
      this.drone = res.data.result
    })
    .catch (err => {
      console.log(err)
    })
  },
  mounted() {
    window.addEventListener('scroll', this.detectWindowScrollY)
  },
  methods: {
    detectWindowScrollY() {
      // if(window.scrollY > this.Rental.getBoundingClientRect().top + window.pageYOffset) {
      // }
    }
  }
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
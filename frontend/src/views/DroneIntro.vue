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
        <ul class="mb-5">
          <li>실내에 최적화된 크기와 무게</li>
          <li>비상착륙 기능 등 높은 안전성</li>
          <li>최대 15분 비행 가능한 배터리 용량</li>
          <li>720p 화질의 카메라</li>
          <li>고도측정 가능</li>
        </ul>
        <div>CATCHCAM은 오브젝트 추적 자율 주행 촬영 드론으로, 실내 촬영에 안성맞춤입니다. 비상착륙, 정밀한 호버링, 고도 측정 등 높은 안정성을 지닌 기능을 제공하고 있죠. 게다가 최대 15분 비행이 가능한 배터리 용량을 가지고 있으며 720p 화질의 영상을 지원합니다. 
 CATCHCAM과 함께라면 그 어느 때보다 즐거운 경기가 가능합니다!</div>

        <div class="subtitle">사용 방법</div>
          <iframe width="720" height="486" class="embed-responsive-item" type="text/html" :src="videoUrl" frameborder="0"></iframe>
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
        <Rental :drone="drone" v-bind:class="{ sticky: isSticky }"/>
      </v-col>
    </v-row>
    <Footer/>
  </v-container>
</template>

<script>
import axios from 'axios'
import Rental from '@/components/droneintro/Rental'
import Reviews from '@/components/droneintro/Reviews'
import Footer from '@/components/Footer'
import http from '@/api/api.js'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
// const API_KEY = 'AIzaSyBiEadK_9db-e-iOFm8K-PCYGYovrl8Tho'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'


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
      isSticky: false,
      videoUrl: null,
    };
  },
  filters: {
    comma: function(value) {
      var num = new Number(value);
      return num.toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, ",")
    }
  },
  created () {
    console.log('여길봐')
    console.log(process.env.VUE_APP_YOUTUBE_API_KEY)
    http.axios.get('/item/1') 
    .then (res => {
      this.drone = res.data.result
    })
    .catch (err => {
      console.log(err)
    })
    // 동영상
    axios.get(API_URL, {
      params: {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: 'CATCHCAM 사용방법',
      }
    })
    .then( res => {
      console.log(res.data.items[0].id.videoId)
      const videoId = res.data.items[0].id.videoId
      this.videoUrl = `https://www.youtube.com/embed/${videoId}`
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
  margin-top: 72px;
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
.sticky {
  position: fixed;
  top: 0;
  width: 100%;
}
</style>
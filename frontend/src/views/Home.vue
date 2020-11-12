<template>
  <div id="app">
    
    <v-img
      class="section head-image text-center align-center"
      :src="randomImage"
    >
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(1)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-img>

    <v-container class="section align-center justify-center" fluid>
      <v-row class="justify-center my-15 pt-10">
        <div class="text-h4">언제 CatchCam을 사용하나요?</div>
      </v-row>
      <v-row class="d-flex justify-center">
        <v-card
        width="300px"
        height="300px"
        color="#23252d"
        flat
        class="d-flex flex-column align-center justify-center mx-3"
        > 
          <v-img
            class="icon"
            src="@/assets/home/011-soccer field.png"
          ></v-img>
          <v-card-title class="white--text explain">
            경기 분석이 필요할 때
          </v-card-title>
        </v-card>
        <v-card
        width="300px"
        height="300px"
        color="#23252d"
        flat
        class="d-flex flex-column align-center justify-center mx-3"
        > 
          <v-img
            class="icon"
            src="@/assets/home/036-soccer.png"
          ></v-img>
          <v-card-title class="white--text explain">
            경기하는 내 모습을 간직하고 싶을 때
          </v-card-title>
        </v-card>
        <v-card
        width="300px"
        height="300px"
        color="#23252d"
        flat
        class="d-flex flex-column align-center justify-center mx-3"
        > 
          <v-img
            class="icon"
            src="@/assets/home/015-team bench.png"
          ></v-img>
          <v-card-title class="white--text explain">
            경기를 녹화해 줄 인력이 부족할 때
          </v-card-title>
        </v-card>
        <v-card
        width="300px"
        height="300px"
        color="#23252d"
        flat
        class="d-flex flex-column align-center justify-center mx-3"
        > 
          <v-img
            class="icon"
            src="@/assets/home/008-yellow card.png"
          ></v-img>
          <v-card-title class="white--text explain">
            경기 판정이 애매할 때
          </v-card-title>
        </v-card>
      </v-row>

      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(2)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-container>    

    <v-img
      class="section head-image text-center align-center"
      src="@/assets/main2.png"
    >
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(3)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-img>
    <v-img
      class="section head-image text-center align-center"
      src="@/assets/main3.png"
    >
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(4)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-img>

    <!-- 사용자 리뷰 -->
    <v-container class="section align-center justify-center" fluid>
      <v-row class="justify-center my-15 pt-10">
        <div class="text-h4">실제 사용자들의 후기</div>
      </v-row>
      <v-row class="d-flex justify-center">
        <v-card
        v-for="review in reviews"
        :key="review.id"
        width="300px"
        height="300px"
        color="#23252d"
        flat
        class="d-flex flex-column align-start justify-center mx-3"
        > 
          <v-card-title class="white--text explain pb-3">
            {{ review.userName }}
          </v-card-title>
          <v-card-subtitle class="date-text pb-0" style="color:rgb(148, 148, 148);">
            {{ review.strCreateDate }}
          </v-card-subtitle>
          <v-rating
            :value="review.starRate"
            readonly
            color="yellow darken-3"
            background-color="grey darken-1"
            empty-icon="$ratingFull"
            dense
            size="15"
            class="pl-3"
          ></v-rating>
          <v-card-text class="white--text pt-2">
            {{ review.content }}
          </v-card-text>
        </v-card>
      </v-row>

      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(5)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-container>

    <v-container class="section align-center justify-center" fluid>
      <div class="d-flex justify-center align-center">
        <div class="drone-wrapper">
          <v-img
          class="section head-image text-center align-center"
          style="height:auto;"
          src="@/assets/drone3.png"
          ></v-img>
        </div>
        <div class="mr-15">
          <div class="text-h4">
            CATCHCAM을 <br>지금 바로 시작해보세요!
          </div>
          <div class="mt-3">
            간단한 절차를 통해 CATCHCAM을 사용할 수 있습니다. <br> 대여 페이지에서 대여와 관련된 자세한 정보를 확인하세요. 
          </div>
          <div>
            <v-btn
            class="mt-10"
            color="#018F26"
            dark
            rounded
            large
            @click="$router.push({name: 'Login'})"
            >로그인하고 대여하기</v-btn>
          </div>
        </div>
      </div>   
      <div class="d-flex flex-column justify-center align-center mt-12">
        <p class="footer1">
          고객센터(이용 및 결제 문의) ssafy@ssafy.com · 02-000-0000
        </p>        
        <p class="footer2">
          주식회사 181 / 서울특별시 강남구 역삼동 테헤란로 212 멀티캠퍼스 / 대표번호 02-000-0000
        </p>
      </div> 
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollToTop()"
          ><v-icon x-large>mdi-arrow-up</v-icon>
      </v-btn>
    </v-container>
  </div>
</template>
<script>
// @ is an alias to /src

export default {
  name: "Home",
  data() {
    return {
      images: [
        require("@/assets/main_img.png"),
        // require("@/assets/main_img2.jpg"),
        // require("@/assets/main_img3.jpg"),
      ],
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
      captions: [
        {
          caption: "경기 분석이 필요할 때",
          image: "@/assets/home/011-soccer field.png",
        },
        {
          caption: "경기하는 내 모습을 간직하고 싶을 때",
          image: "036-soccer"
        },
        {
          caption: "경기를 녹화해 줄 인력이 부족할 때",
          image: "015-team bench"
        },
        {
          caption: "경기 판정이 애매할 때",
          image: "008-yellow card"
        },
      ],
      reviews: [
        { 
          id: 1,
          userName: '예슬짱',
          strCreateDate: '2020-11-12',
          starRate: 5,
          content: '고게 졸졸 따라오는데 신기했어요 제가 마치...축구 선수가 된 것 같은 기분..너무 짜릿했어요 어떻게 이런걸 만들었대요? 요즘 애들 참 대단해 취업한다~공부한다~ 우리땐 안그랬는데',
        },
        {
          id: 2,
          userName: '예슬짱',
          strCreateDate: '2020-11-12',
          starRate: 5,
          content: '고게 졸졸 따라오는데 신기했어요 제가 마치...축구 선수가 된 것 같은 기분..너무 짜릿했어요 어떻게 이런걸 만들었대요? 요즘 애들 참 대단해 취업한다~공부한다~ 우리땐 안그랬는데',
        },
        {
          id: 3,
          userName: '예슬짱',
          strCreateDate: '2020-11-12',
          starRate: 5,
          content: '고게 졸졸 따라오는데 신기했어요 제가 마치...축구 선수가 된 것 같은 기분..너무 짜릿했어요 어떻게 이런걸 만들었대요? 요즘 애들 참 대단해 취업한다~공부한다~ 우리땐 안그랬는데',
        }
      ]
    };
  },
  computed: {
    randomImage() {
      let index = Math.floor(Math.random() * this.images.length);
      return this.images[index];
    },
  },
  methods: {
    scrollDown(idx) {
      window.scrollTo({
        top: idx * window.innerHeight,
        behavior: "smooth",
      });
    },
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
  },
};
</script>
<style scoped>
@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSans-kr.css);
* {
  font-family: "Spoqa Han Sans", "Sans-serif";
}
.icon {
  width: auto; height: auto;
  max-height: 100px;
  max-width: 100px;
}
.explain {
  font-size: 17px;
}
.intro_title {
  font-size: 24px;
  font-weight: bold;
}
.intro_content {
  padding: 20px 0;
}
.drone-wrapper {
  width: 40%;
}
.section {
  position: relative;
  height: 100vh;
  color: white;
}
.footer1 {
  font-size: 14px;
  color:rgb(160, 160, 160);
  margin: 0;
}
.footer2 {
  font-size: 13px;
  color:gray;
  margin: 0;
}
.circle {
  width: 20vw;
  height: 20vw;
  background-color: rgb(198 214 242);
  border-radius: 50%;
  margin-top: -40vh;
}

.caption {
  width: 20vw;
}

.head-image {
  /* filter: brightness(70%); */
}

.main-btn {
  bottom: 14vh;
  left: 50%;
  transform: translateX(-50%);
}
.date-text {
  color:rgb(148, 148, 148);
  font-size: 12px;
}
</style>
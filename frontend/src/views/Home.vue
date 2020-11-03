<template>
  <div id="app">
    <!-- <v-carousel
      cycle="cycle"
      hide-delimiters
      interval="7000"
      :show-arrows="false"
      height="100vh"
      class=""
    >
      <v-carousel-item v-for="(image, i) in images" :key="i" :src="image">
      </v-carousel-item>
    </v-carousel> -->

    <v-img
      class="section head-image text-center align-center"
      :src="randomImage"
      light
    >
      <div class="text-h1 image-text">CatchCam</div>
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(1)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-img>

    <v-container fluid class="section">
      <div class="text-h2 text-center my-5">CatchCam 소개</div>

      <v-sheet
        elevation="24"
        height="60vh"
        width="80vw"
        class="mx-auto mt-10"
      ></v-sheet>
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(2)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-container>

    <v-container class="section justify-center align-center" fluid fill-height>
      <div class="text-h3">언제 CatchCam을 사용하나요?</div>
      <v-row>
        <v-col
          cols="12"
          sm="6"
          md="3"
          v-for="(caption, i) in captions"
          :key="i"
        >
        <div class="circle"></div>
        <div class="text-center text-subtitle-1 caption">{{ caption }}</div>
        </v-col>
      </v-row>
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(3)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-container>

    <v-container class="section" fluid>
      <v-row>
        <v-col cols="6">
          <h2>드론 초심자도</h2>
          <h3>자율 주행으로 공을 추적하며 경기를 촬영합니다.</h3>
        </v-col>
        <v-col cols="6">
          <v-img src="../assets/main_img3.jpg"></v-img>
        </v-col>
      </v-row>
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollDown(4)"
        ><v-icon x-large>mdi-arrow-down</v-icon></v-btn
      >
    </v-container>

    <v-container class="section" fluid>
      <v-row>
        <v-col cols="6">
          <v-img src="../assets/main_img2.jpg"></v-img>
        </v-col>
        <v-col cols="6">
          <h2>다양한 각도와 방향에서</h2>
          <h3>CatchCam은 드론으로 공중에서 촬영합니다.</h3>
        </v-col>
        
      </v-row>
      <v-btn fab absolute outlined dark class="main-btn" @click="scrollToTop()"
        ><v-icon x-large>mdi-arrow-up</v-icon></v-btn
      >
    </v-container>

    <!--     
        <v-flex style="margin-top: 70px" >
          <v-row>
            <v-col cols="8" align-self="center">
                <div class="intro_title">드론 초심자도</div>
                <div class="intro_content">
                  자율 주행으로 공을 추적하며 경기를 촬영합니다.
                </div>
            </v-col>
            <v-col cols="4">
              <div
                style="
                  width: 200px;
                  height: 200px;
                  background-color: rgb(198 214 242);
                "
              ></div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="8" align-self="center">
              <v-row>
                <div class="intro_title">다양한 각도와 방향에서</div>
              </v-row>
              <v-row>
                <div class="intro_content">
                  CatchCam은 드론으로 공중에서 촬영합니다.
                </div>
              </v-row>
            </v-col>
            <v-col cols="4">
              <div
                style="
                  width: 200px;
                  height: 200px;
                  background-color: rgb(198 214 242);
                "
              ></div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="8" align-self="center">
              <v-row>
                <div class="intro_title">유튜브 플랫폼을 활용한</div>
              </v-row>
              <v-row>
                <div class="intro_content">
                  유튜브 동영상 플랫폼을 활용해 경기 녹화 영상을 라이브
                  방송하거나, 혹은 저장하여 간직할 수 있습니다.
                </div>
              </v-row>
            </v-col>
            <v-col cols="4">
              <div
                style="
                  width: 200px;
                  height: 200px;
                  background-color: rgb(198 214 242);
                "
              ></div>
            </v-col>
          </v-row>
        </v-flex>
        <v-flex style="margin: 70px 0; text-align: center">
          <v-btn rounded dark large color="#07B480">로그인하고 대여하기</v-btn>
        </v-flex>
      </v-layout>
    </v-container> -->
  </div>
</template>
<script>
// @ is an alias to /src

export default {
  name: "Home",
  data() {
    return {
      images: [
        require("@/assets/main_img1.png"),
        require("@/assets/main_img2.jpg"),
        require("@/assets/main_img3.jpg"),
      ],
      captions: [
        "경기 분석이 필요할 때",
        "경기하는 내 모습을 간직하고 싶을 때",
        "경기를 녹화해 줄 인력이 부족할 때",
        "경기 판정이 애매할 때",
      ],
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

.intro_title {
  font-size: 24px;
  font-weight: bold;
}

.intro_content {
  padding: 20px 0;
}

.section {
  position: relative;
  height: 100vh;
  color: white;
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
  bottom: 10vh;
  left: 50%;
  transform: translateX(-50%);
}
</style>
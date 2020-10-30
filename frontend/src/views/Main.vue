<template>
  <div id="app">
    <v-carousel
      cycle="cycle"
      height="400"
      hide-delimiter-background="hide-delimiter-background"
      interval="7000"
    >
      <v-carousel-item v-for="(image, i) in images" :key="i">
        <v-sheet
          height="100%"
          style="background-color: rgba(135, 206, 235, 0.26)"
        >
          <v-row
            justify="start"
            align="center"
            style="max-width: 1180px; margin: 0px auto; height: 400px"
          >
            <v-col :cols="6">
              i = {{ image }}
              <v-img :src="`${image}`" height="400" contain="contain" />
            </v-col>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
    <v-container>
      <v-layout column="column">
        <v-flex>
          <div
            style="
              margin: 40px 0 20px 0;
              font-size: 24px;
              font-weight: bold;
              width: 100%;
              text-align: center;
            "
          >
            CatchCam 소개
          </div>
        </v-flex>
        <v-flex>
          <div style="width: 100%; text-align: center">
            <div
              style="
                margin: auto;
                width: 200px;
                height: 200px;
                background-color: rgb(198 214 242);
              "
            ></div>
          </div>
        </v-flex>
        <v-flex>
          <div
            style="
              margin: 60px 0 20px 0;
              width: 100%;
              font-size: 20px;
              font-weight: bold;
              text-align: center;
            "
          >
            왜 CatchCam을 사용하나요?
          </div>
        </v-flex>
        <v-flex>
          <v-row>
            <v-col cols="12" sm="6" md="3">
              <div
                style="
                  margin: auto;
                  width: 200px;
                  height: 200px;
                  background-color: rgb(198 214 242);
                  border-radius: 50%;
                "
              ></div>
              <div style="text-align: center">경기 분석이 필요할 때</div>
            </v-col>
            <v-col cols="12" sm="6" md="3">
              <div
                style="
                  margin: auto;
                  width: 200px;
                  height: 200px;
                  background-color: rgb(198 214 242);
                  border-radius: 50%;
                "
              ></div>
              <div style="text-align: center">
                경기하는 내 모습을<br />간직하고 싶을 때
              </div>
            </v-col>
            <v-col cols="12" sm="6" md="3">
              <div
                style="
                  margin: auto;
                  width: 200px;
                  height: 200px;
                  background-color: rgb(198 214 242);
                  border-radius: 50%;
                "
              ></div>
              <div style="text-align: center">
                경기를 녹화해 줄<br />인력이 부족할 때
              </div>
            </v-col>
            <v-col cols="12" sm="6" md="3">
              <div
                style="
                  margin: auto;
                  width: 200px;
                  height: 200px;
                  background-color: rgb(198 214 242);
                  border-radius: 50%;
                "
              ></div>
              <div style="text-align: center">경기 판정이 애매할 때</div>
            </v-col>
          </v-row>
        </v-flex>
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
        "@/assets/main_img1.png",
        "@/assets/main_img2.jpg",
        "@/assets/main_img3.jpg",
      ],
    };
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
</style>
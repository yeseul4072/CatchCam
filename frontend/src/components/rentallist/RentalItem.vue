<template>
  <v-card
    color="#23252d"
    class="ma-3"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      :src="rentalItem.item.profile_img"
    ></v-img>
    <v-card-text class="py-0">
      <v-row
        align="center"
        class="mx-0"
      >
        <div class="grey--text font-weight-light">
          {{ rentalItem.rent_date }} ~ {{ rentalItem.return_date }}
        </div>
      </v-row>
    </v-card-text>
    <div class="d-flex justify-space-between">
      <v-card-title class="white--text py-0">{{ rentalItem.item.item_name }}</v-card-title>
      <div class="white--text my-1 mx-5" style="font-size:1.2rem;">
        ₩{{ rentalItem.cost }}
      </div>
    </div>

    <!-- <v-divider class="mx-4"></v-divider> -->
    <v-card-actions class="d-flex flex-column">
      <v-btn
        text
        block
        class="white--text d-flex justify-space-between mb-5"
      >
      <div>{{ rentalItem.store.store_name }}</div>
      <div class="gray_text font-weight-light">자세히 보기 ></div>
        
      </v-btn>
      <div class="align-self-end ma-2">
        <v-btn
          color="#018F26"
          @click="reserve"
          dark
          outlined
          class="mr-2"
        >
          대여 수정
        </v-btn>
        <v-btn
          color="#018F26"
          @click="reserve"
          dark
        >
          대여 취소
        </v-btn>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "RentalItem",
  props: {
    rentalItem: {
      type: Object
    }
  }
}
</script>

<style scoped>
.title {
  font-size: 2rem;
}
.gray_text {
  font-size: 0.8rem;
  color: rgb(148, 148, 148);
}
.my-img {
  background-color: white;
}
.img_wrap {
  width: 80%;
}
.content_text {
  color: white;
}
</style>
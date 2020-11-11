<template>
  <v-card
    color="#23252d"
    class="ma-3 my-card"
    max-width="374"
    @click="$router.push({name:'DroneIntro'})"
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
      src="@/assets/drone4.png"
    ></v-img>
    <v-card-text class="py-0">
      <v-row
        align="center"
        class="mx-0"
      >
        <div class="grey--text font-weight-light">
          {{ rentalItem.strRentDate }} ~ {{ rentalItem.strReturnDate }}
        </div>
      </v-row>
    </v-card-text>
    <div class="d-flex justify-space-between align-center">
      <div class="d-flex align-center">
        <v-card-title class="white--text py-0 pr-2">
          {{ rentalItem.itemName }}
          <v-chip class="ml-2" small color="#018F26" outlined>{{ rentalItem.status }}</v-chip>
        </v-card-title>
      </div>
      <div class="white--text my-1 mx-5" style="font-size:1.2rem;">
        ₩{{ rentalItem.cost }}
      </div>
    </div>

    <!-- <v-divider class="mx-4"></v-divider> -->
    <v-card-actions class="d-flex flex-column">
      <v-btn
        text
        block
        class="white--text d-flex justify-space-between"
      >
      <div>{{ rentalItem.storeName }}</div>
      <div class="gray-text font-weight-light">자세히 보기 ></div>
        
      </v-btn>
    
    </v-card-actions>
    <v-card-actions class="d-flex flex-row-reverse">
      <div v-if="rentalItem.status=='예약중'" class="ma-3">
        <v-btn
          outlined
          color="red"
          @click="reserve"
        >
          예약 취소
        </v-btn>
      </div>
      <div v-if="rentalItem.status=='대여중' || rentalItem.status=='반납완료'" class="ma-3">
        <v-btn
          color="white"
          @click="reserve"
          dark
          outlined
        >
          후기 작성
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
.gray-text {
  font-size: 0.8rem;
  color: rgb(148, 148, 148);
}
.my-img {
  background-color: white;
}
.my-card {
  cursor: pointer;
}
</style>
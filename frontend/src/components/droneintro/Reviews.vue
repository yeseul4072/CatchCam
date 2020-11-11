<template>
  <div>
    <v-card v-if="showReviewForm" outlined color="#23252d" class="mb-5" style="border: 1px solid rgb(148, 148, 148);">
      <v-container class="d-flex flex-column">
      <v-textarea
        color="rgb(148, 148, 148)"
        counter
        dark
        flat
        v-model="reviewData.content"
      ></v-textarea>
      <div class="d-flex justify-space-between align-center">
        <div class="d-flex align-center">
          <div class="reg_text">별점: </div>
          <v-rating
            class="align-self-end"
            v-model="reviewData.star_rate"
            color="yellow darken-3"
            background-color="grey darken-1"
            empty-icon="$ratingFull"
            half-increments
            hover
            dense
            size="18"
          ></v-rating>
        </div>
        <div class="d-flex align-self-end">
          <v-btn
            color="#018F26"
            outlined
            dark
            class="mr-2"
            @click="reviewForm()"
          >취소하기</v-btn>
          <v-btn
            color="#018F26"
            dark
            @click="createReview()"
          >저장하기</v-btn>
        </div>
        </div>
      </v-container>
    </v-card>

    <div class="d-flex justify-space-between align-center">
      <div class="d-flex">
        <div class="score_text">
          이용후기 <span class="colored_text">{{ count }}개</span>
        </div>
        <div class="mx-2">
          ·
        </div>
        <div class="score_text">
          평균평점 <span class="colored_text">{{ avg_rate }}</span>
        </div>
      </div>
      <div>
        <v-btn color="#018F26" dark @click="reviewForm()" v-if="!showReviewForm">후기 쓰기</v-btn>
      </div>
    </div>
    <ReviewItem
    class="mt-3"
    v-for="review in reviews"
    :key="review.id"
    :review="review"
    @updateData="updateData"
    />
  </div>
</template>

<script>
import ReviewItem from '@/components/droneintro/ReviewItem'
import http from '@/api/api.js'

export default {
  name: "Reviews",
  components: {
    ReviewItem,
  },
  data() {
    return {
      showReviewForm: false,
      reviews: [
        {
          avg_rate: null,
          count: null,
          review_yn: false,
          reviews: null
        }
      ],
      reviewData: {
        content: null,
        item_id: null,
        star_rate: null,
      }
    }
  },
  created: function() {
    http.axios.get('/reviews/1') 
    .then( res => {
      this.avg_rate = res.data.result.avgRate,
      this.count = res.data.result.reviewCount,
      this.review_yn = res.data.result.reviewYn
      this.reviews = res.data.result.reviews
    })

  },
  methods: {
    reviewForm() {
      this.showReviewForm = !this.showReviewForm
    },
    updateData(updateData) {
      this.reviewForm()
      this.reviewData.id = updateData.id,
      this.reviewData.item_id = updateData.item_id,
      this.reviewData.user_id = updateData.user_id,
      this.reviewData.content = updateData.content,
      this.reviewData.star_rate = updateData.star_rate
    },
    createReview() {
      http.axios.post('/review', this.reviewData)
      .then( res => {
        console.log(res)
      })
    }
  }

}
</script>

<style scoped>
.score_text {
  font-size: 18px;
}
.reg_text {
  color: white;
}
.colored_text {
  color: #018F26;
  font-weight: bold;
}
</style>
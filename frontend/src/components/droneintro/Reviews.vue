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
          >저장하기</v-btn>
        </div>
        </div>
      </v-container>
    </v-card>

    <div class="d-flex justify-space-between align-center">
      <div class="score_text">
        {{ reviews[0].avg_rate }} / 5 ({{ reviews[0].count }}개 후기)
      </div>
      <div>
        <v-btn color="#018F26" dark @click="reviewForm()" v-if="!showReviewForm">후기 쓰기</v-btn>
      </div>
    </div>
    <ReviewItem
    class="mt-3"
    v-for="review in reviews[0].reviews"
    :key="review.id"
    :review="review"
    @updateData="updateData"
    />
  </div>
</template>

<script>
import ReviewItem from '@/components/droneintro/ReviewItem'

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
          avg_rate: 2,
          count: 2,
          review_yn: true,
          reviews:
          [
            {
              id: 0,
              item_id: 0,
              user_name: '허예슬',
              content: '내용',
              create_date: '2020-11-9',
              modify_date: '2020-11-9',
              star_rate: 1,
              writer_yn: true
            },
            { 
              id: 1,
              item_id: 0,
              user_name: '몽똥이',
              content: '내용2',
              create_date: '2020-11-9',
              modify_date: '2020-11-9',
              star_rate: 3,
              writer_yn: false
            }
          ]
        }
      ],
      reviewData: {
        id: null,
        item_id: null,
        user_id: null,
        content: null,
        star_rate: null,
      }
    }
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
    }
  }

}
</script>

<style scoped>
.score_text {
  font-size: 20px;
  font-weight: bold;
}
.reg_text {
  color: white;
}
</style>
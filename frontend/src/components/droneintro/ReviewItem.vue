<template>
  <div>
    <hr class="my-hr">
    <div class="my-3">
      <div class="d-flex justify-space-between">
        <div class="d-flex">
          <div>{{ review.user }}</div>
          <div class="date-text">{{ review.create_date }}</div>
        </div>
        <v-rating
          :value="review.star_rate"
          readonly
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          size="15"
        ></v-rating>
      </div>
      <div>
        {{ review.content }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewItem",
  props: {
    review: {
      type: Object
    }
  }
}
</script>

<style scoped>
.date-text {
  color:rgb(148, 148, 148);
  margin-left: 1rem;
  font-size: 14px;
}
.my-hr {
  border: 0;
  height: 1px;
  background-color:rgb(148, 148, 148);
}

</style>
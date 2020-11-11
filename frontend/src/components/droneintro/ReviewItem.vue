<template>
  <div>
    <hr class="my-hr">
    <div class="my-3">
      <div class="d-flex justify-space-between">
        <div class="d-flex align-center">
          <div>{{ review.userName }}</div>
          <div class="date-text">{{ review.strCreateDate }}</div>
          <v-rating
            :value="review.starRate"
            readonly
            color="yellow darken-3"
            background-color="grey darken-1"
            empty-icon="$ratingFull"
            dense
            size="15"
            class="ml-5"
          ></v-rating>
        </div>

        <!-- 수정/삭제 버튼 -->
        <div v-if="review.writerYn" class="text-center">
          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="#8d8d8d" icon dark v-bind="attrs" v-on="on">
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="update()">
                <v-list-item-title>수정</v-list-item-title>
              </v-list-item>
              <v-list-item @click="del()">
                <v-list-item-title>삭제</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </div>
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
  data() {
    return {
      updateData: {
        id: this.review.id,
        item_id: this.review.item_id,
        user_id: this.review.user_id,
        content: this.review.content,
        star_rate: this.review.star_rate,
      }
    }
  },
  props: {
    review: {
      type: Object
    }
  },
  methods: {
    update() {
      this.$emit("updateData", this.updateData);
    },
    del() {

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
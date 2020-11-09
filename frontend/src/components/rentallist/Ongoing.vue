<template>
  <v-container fluid>
    <RentalItem
    v-for="rentalItem in rental_list"
    :key="rentalItem.id"
    :rentalItem="rentalItem"
    />
  </v-container>
</template>

<script>
import RentalItem from '@/components/rentallist/RentalItem'


export default {
  name: "Ongoing",
  components: {
    RentalItem
  },
  data() {
    return {
      rental_list: [
        {
          id: 0,
          rent_date: '2020-11-09',
          return_date: '2020-11-10',
          cost: 50000,
          item: {
            item_name: '왱왱v1',
            profile_img: require('@/assets/drone4.png')
          },
          store: {
            store_name: '왱왱스토어',
            tel_no: '010-4940-4072',
            open_time: 9,
            close_time: 18,  
            address: '주소'
          }
        },
      ]
    }
  }
}
</script>

<style scoped>

</style>
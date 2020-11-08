<template>
  <v-card class="Rental">
     <v-card-subtitle class="subtitle">지점 선택</v-card-subtitle>
      <div>
        <v-container class="py-0">
          <v-row >
            <v-col cols="6" class="pr-0">
              <v-combobox
                v-model="city"
                :items="cities"
                label="시/도"
                outlined
                dense
              ></v-combobox>
            </v-col>
            <v-col cols="6" class="pl-0">
              <v-combobox
                v-model="district"
                :items="districts"
                label="군/구"
                outlined
                dense
              ></v-combobox>
            </v-col>
          </v-row>
        </v-container>

        <v-card
          outlined
          max-width="400"
          class="mx-auto d-flex flex-column justify-center"
        > 
          <v-virtual-scroll
            :items="stores"
            item-height="64"
          >
            <template v-slot:default="{ item }">
              <v-list-item :key="item.store_id">
                <v-list-item-content>
                  <v-list-item-title>
                    <strong>{{ item.store_name }}</strong> {{ item.tel_no }}
                  </v-list-item-title>
                  <v-list-item-title class="sm-content">
                    {{ item.address }}
                  </v-list-item-title>
                </v-list-item-content>

                <v-list-item-action>
                  <v-btn
                    text
                    depressed
                  > 
                  <div class="icon-wrap">
                    <v-img
                      src="@/assets/map.png"
                    ></v-img>
                  </div>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>

              <v-divider></v-divider>
            </template>
          </v-virtual-scroll>

    <v-card-subtitle class="subtitle mt-5">날짜 선택</v-card-subtitle>
      <div class="d-flex justify-center">
        <v-card class="btn-text" @click="getCalendar()">
          <v-card-title class="btn-title">시작일</v-card-title>
          <v-card-subtitle v-if="dates[0]">{{dates[0]}}</v-card-subtitle>
          <v-card-subtitle v-else>날짜추가</v-card-subtitle>
        </v-card>
        <v-card class="btn-text" @click="getCalendar()">
          <v-card-title class="btn-title">반납일</v-card-title>
          <v-card-subtitle v-if="dates[1]">{{dates[1]}}</v-card-subtitle>
          <v-card-subtitle v-else>날짜추가</v-card-subtitle>
        </v-card>
      </div>
      <!-- calendar -->
      <v-card-text>
        <v-row v-if="showCalendar" justify="center">
            <v-date-picker
              full-width
              v-model="dates"
              range
            ></v-date-picker>
        </v-row>
      </v-card-text>
      
      <div v-if="cost">
        <v-card-subtitle class="subtitle">가격</v-card-subtitle>
        <v-card-text class="d-flex flex-column">
          <div class="d-flex justify-sm-space-between">
            <div>
              대여료 
            </div>
            <strong>
              ₩{{ drone.cost }} × {{ term }}일
            </strong>
          </div>
          <hr class="my-3">
          <div class="emp-text align-self-end">
            ₩{{ cost }}
          </div>
        </v-card-text>
      </div>

     
          <v-btn
          class="ma-3 my-5"
          color="#018F26"
          dark
          large
          @click="$router.push({name: 'Login'})"
          >대여 신청하기</v-btn>
        </v-card>
      </div>
  </v-card>
    
</template>

<script>

export default {
  name: "Rental",
  data() {
    return {
      dates: [],
      term: null,
      cost: null,
      showCalendar: false,
      cities: ['서울', '부산'],
      city: null,
      districts: ['동대문구', '관악구'],
      district: null,
      stores: [{'store_id': 1, 'store_name': '명동점', 'tel_no': '010-4940-4072', 'open_time': 9, 'close_time': 18, 'latitude': 20.0, 'longitude': 30.0, 'address': '서울특별시 중구 마른내로 47 (초동)'}, {'store_id': 1, 'store_name': '신당점', 'tel_no': '010-4940-4072', 'open_time': 9, 'close_time': 18, 'latitude': 20.0, 'longitude': 30.0, 'address': '서울특별시 중구 다산로 156 (신당동)'}],
    };
  },
  props: {
    drone: {
      type: Object,
    }
  },
  watch: {
    'dates': function() {
      if (this.dates[1]) {
        this.getCalendar()
        var arr1 = this.dates[0].split('-')
        var d1 = new Date(arr1[0], arr1[1], arr1[2])
        var arr2 = this.dates[1].split('-')
        var d2 = new Date(arr2[0], arr2[1], arr2[2])
        var currDay = 24 * 60 * 60 * 1000
        this.term = parseInt((d2 - d1)/currDay)
        this.cost = this.term * this.drone.cost 
      }
    }
  },
  computed: {
    dateRangeText () {
      return this.dates.join(' ~ ')
    },
    items () {
        return Array.from({ length: this.length }, (k, v) => v + 1)
    },
    length () {
      return 5
    },
  },
  methods: {
    getCalendar() {
      this.showCalendar = !this.showCalendar
    }
  }

}
</script>

<style scoped>
.btn-title {
  font-size: 15px;
  color: black;
  font-weight: bold;

}
.btn-text {
  color: rgb(148, 148, 148);
  width:45%;
  cursor:pointer;
}
.subtitle {
  font-size: 17px;
  color: black;
  font-weight: bold;
}
.sm-content {
  font-size: 13px;
}
.icon-wrap {
  width: 80%;
}
.emp-text {
  color: #018F26;
  font-size: 20px;
  font-weight: bold;
}
</style>
import Vue from "vue"
import axios from "axios";

export default new Vue({
  computed: {
    token() {
       return sessionStorage.getItem('Token');
    },
    axios() {
      return axios.create({
        baseURL: "http://k3a102.p.ssafy.io:8000/api",
        headers: {
          "x-auth-token": this.token ? this.token : '',
          "Content-type": "application/json"
        }
      });
    }
  } 
}); 
<template>
    <v-container class="container" fill-height style="max-width:380px">
        <v-laytout align-center justify-center row wrap style="width:100%;">
            <v-flex xs12>
                <v-card flat>
                    <!-- 로고 -->
                    <div class="pa-3 mb-5 d-flex justify-center align-center">
                        <div style="width:25%;">
                            <v-img
                            src="@/assets/drone2.png"
                            width="100%"
                            right
                            center
                            >    
                            </v-img>
                        </div>
                        <div>
                            <h1 class="logo-text">CatchCam</h1>
                            <h3 class="mb-0 grey--text font-weight-light">Catch me if you cam</h3>
                        </div>
                    </div>
                    <!-- 폼 -->
                    <div class="pa-3">
                        <v-text-field
                        v-model="email"
                        label="이메일"
                        ></v-text-field>
                        <v-text-field
                        v-model="password"
                        type="password"
                        label="비밀번호"
                        ></v-text-field>
                        <v-checkbox
                        v-model="saveId"
                        label="아이디 저장"
                        color="#07B480"
                        value="primary"
                        hide-details
                        class="mt-0"
                        ></v-checkbox>
                    </div>
                    <!-- 버튼 -->
                    <v-card-actions class="mt-2">
                        <v-btn 
                            class="login_btn"
                            block
                            large
                            color="#07B480"
                            @click="login(email, password)"
                            :disabled="!isComplete"
                        >
                            로그인
                        </v-btn>
                    </v-card-actions>
                    <div class="d-flex justify-center mt-2">
                        <router-link to="/signup" class="text-decoration-none grey--text">회원가입</router-link>
                        <router-link to="" class="ml-3 text-decoration-none grey--text">아이디·비밀번호 찾기</router-link>
                    </div>
                </v-card>
            </v-flex>
        </v-laytout>
    </v-container>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            email: null,
            password: null,
            saveId: false,
            isComplete: false,
        }
    },
    watch: {
        'email': function() {
            this.checkAll()
        },
        'password': function() {
            this.checkAll()
        }
    },
    methods: {
        checkAll() {
            if (this.email && this.password) {
                this.isComplete = true
            } else {
                this.isComplete = false
            }
        },
        login(email, password) {
            axios.post(`http://localhost:?/login`, {
                email: email,
                password: password
            })
            .then(res => {
                sessionStorage.setItem("Token", res.data.object)
                this.$router.push({name: 'Main'})
            })
            .catch(err => {
                alert(`${err}를 확인해주세요`)
            })
        }
    }
    
}
</script>

<style scoped>
.logo-text {
    font-size: 2em;
}
.login_btn {
    color:white;
}
</style>
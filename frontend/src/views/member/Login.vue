<template>
    <v-container class="container" fill-height style="max-width:380px">
        <v-laytout align-center justify-center row wrap style="width:100%;">
            <v-flex xs12>
                <v-card flat>
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
                        v-model="saveid"
                        label="아이디 저장"
                        color="#07B480"
                        value="primary"
                        hide-details
                        class="mt-0"
                        ></v-checkbox>
                    </div>
                    
                    <v-card-actions class="mt-2">
                        <v-btn 
                            block
                            dark
                            large
                            color="#07B480"
                        >
                            로그인
                        </v-btn>
                    </v-card-actions>
                    <div class="d-flex justify-center mt-2">
                        <a href="http://localhost:8080/signup" class="text-decoration-none grey--text">회원가입</a>
                        <a href="" class="ml-3 text-decoration-none grey--text">아이디·비밀번호 찾기</a>
                    </div>
                </v-card>
            </v-flex>
        </v-laytout>
    </v-container>
</template>

<script>


export default {
    data() {
        return {
            email: null,
            password: null,
        }
    }
    
}
</script>

<style scoped>
.logo-text {
    font-size: 2em;
}
</style>
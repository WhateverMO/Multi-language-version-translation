<template>
  <div>
    <div class="center">
      <div class="center1">
        <img src="../../assets/img/welcom.jpeg" />
      </div>
      <div class="center2">
        <h2>作者登录</h2>
        <div class="el-icon-user">
          用户id:<el-input
            v-model="user_id"
            placeholder="请输入你的用户名"
          ></el-input>
        </div>
        <div class="el-icon-key">
          密码 :<el-input
            placeholder="请输入密码"
            v-model="password"
            show-password
          ></el-input>
        </div>
        <el-button type="primary" plain @click="login">立即登录</el-button>
        <div class="register">
          没有账号，<span class="enroll" @click="enroll">点击注册</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import qs from "qs";
import request from "@/request";
export default {
  name: "logincenter",
  data() {
    return {
      password: "",
      user_id: "",
    };
  },
  methods: {
    enroll() {
      this.$router.push("/regestertranslate");
    },
    async login() {
      var data = {
        author_id: this.user_id,
        password: this.password,
      };
      const path = "/api/author/login";
      await request.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$router.push("/author");
          sessionStorage.setItem("id", this.user_id);
          this.$store.commit("id", this.user_id);
        }
      }); //post带参数的登录请求

      await request.get("/api/author/information").then((res) => {
        this.$store.commit("name", res.data.author_name);
        this.$store.commit("age", res.data.author_age);
        this.$store.commit("sex", res.data.author_gender);
        this.$store.commit("place", res.data.author_area);
        this.$store.commit("intro", res.data.author_describe);
      }); //拿作者信息
    },
  },
};
</script>

<style scoped>
.center {
  display: flex;
  justify-content: center;
  height: 60vh;
  margin-top: 10vh;
}
.center2 {
  margin-left: 10vw;
}
img {
  width: 30vw;
  height: 50vh;
}
.el-icon-user,
.el-icon-key {
  display: block;
  margin-bottom: 10vh;
}
h2 {
  text-align: center;
  margin-bottom: 20px;
}
.el-button {
  width: 20vw;
  margin-left: 2vw;
}
.register {
  margin-left: 5vw;
  margin-top: 5vh;
}
.enroll:hover {
  cursor: pointer;
  color: red;
}
.el-input {
  margin-left: 10px;
}
</style>
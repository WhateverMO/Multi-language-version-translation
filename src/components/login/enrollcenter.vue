<template>
  <div class="center">
    <div class="center1">
      <img src="../../assets/img/welcom.jpeg" />
    </div>
    <div class="center2">
      <h2>读者注册</h2>
      <div class="el-icon-user">
        用户名 :<el-input
          v-model="name"
          placeholder="请输入你的用户名"
        ></el-input>
      </div>
      <div class="el-icon-key">
        设置密码 :<el-input
          placeholder="请输入密码"
          v-model="password"
          show-password
        ></el-input>
      </div>
      <div class="el-icon-key">
        确认密码 :<el-input
          placeholder="请再次输入密码"
          v-model="password2"
          show-password
        ></el-input>
      </div>
      <el-button type="primary" plain @click="enroll"> 立即注册</el-button>
      <div class="register">
        有账号，<span class="login" @click="login">点击登录</span>
      </div>
    </div>
  </div>
</template>

<script>
import qs from "qs";
import axios from "axios";
import request from "@/request";
export default {
  name: "enrollcenter",
  data() {
    return {
      password: "",
      name: "",
      password2: "",
    };
  },
  methods: {
    async enroll() {
      var data = {
        username: this.name,
        password: this.password,
        password2: this.password2,
      };
      const path = "/api/user/register";
      await request.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          alert("你的用户id是:" + res.data.user_id);
          this.$store.commit("id", res.data.user_id);
          this.$store.commit("name", this.name);
          this.$store.commit("image", res.data.picture);
          this.$store.commit("sex", "");
          this.$store.commit("place", "");
          this.$store.commit("intro", "");
          this.$store.commit("age", "");
          this.$router.push("/reader");
        }
      }); //用户注册，将用户id存入store
    },
    login() {
      this.$router.push("/loginreader");
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
  margin-bottom: 6vh;
}
h2 {
  text-align: center;
  margin-bottom: 20px;
}
.el-button {
  width: 20vw;
  margin-left: 2vw;
}
.el-input {
  margin-left: 10px;
}
.register {
  margin-left: 5vw;
  margin-top: 5vh;
}
.login:hover {
  cursor: pointer;
  color: red;
}
</style>
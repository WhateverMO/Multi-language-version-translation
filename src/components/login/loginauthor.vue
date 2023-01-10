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
import axios from "axios";
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
      const path = "http://localhost:5000/api/author/login";
      await axios.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$router.push("/author");
          this.$store.commit("id", this.user_id);
        }
      }); //post带参数的登录请求

      await axios
        .get("http://localhost:5000/api/author/information")
        .then((res) => {
          sessionStorage.setItem("id", res.data.author_id);
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
</style>
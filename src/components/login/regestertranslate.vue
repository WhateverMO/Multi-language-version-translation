<template>
  <div class="center">
    <div class="center1">
      <img src="../../assets/img/welcom.jpeg" />
    </div>
    <div class="center2">
      <h2>作者注册</h2>
      <div class="el-icon-user">
        作者名 :<el-input
          v-model="authorname"
          placeholder="请输入你的作者昵称"
        ></el-input>
      </div>
      <div class="el-icon-key">
        密码 :<el-input
          placeholder="请输入密码"
          v-model="password"
          show-password
        ></el-input>
      </div>
      <div class="el-icon-key">
        密码 :<el-input
          placeholder="请再次输入密码"
          v-model="password2"
          show-password
        ></el-input>
      </div>
      <el-button type="primary" plain @click="translator">立即注册</el-button>
      <div class="login">
        有账号，<span class="loginauthor" @click="loginauthor">点击登录</span>
      </div>
    </div>
  </div>
</template>

<script>
import qs from "qs";
import axios from "axios";
export default {
  name: "regestertranslate",
  data() {
    return {
      authorname: "",
      password: "",
      password2: "",
    };
  },
  methods: {
    translator() {
      var data = {
        author_name: this.authorname,
        password: this.password,
        password2: this.password2,
      };
      const path = "http://localhost:5000/api/author/register";
      axios.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$store.commit("id", res.data.author_id);
          alert("你的作者登录id是" + res.data.author_id);
          this.$store.commit("name", this.authorname);
          this.$store.commit("sex", "");
          this.$store.commit("place", "");
          this.$store.commit("intro", "");
          this.$store.commit("age", "");
          this.$router.push("/author");
        }
      }); //用户注册，将用户id存入store
    },
    loginauthor() {
      this.$router.push("/loginauthor");
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
  margin-bottom: 50px;
}
h2 {
  text-align: center;
}
.el-button {
  width: 20vw;
  margin-left: 2vw;
}
.login {
  margin-left: 5vw;
  margin-top: 5vh;
}
.loginauthor:hover {
  cursor: pointer;
  color: red;
}
</style>
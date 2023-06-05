<template>
  <div class="center">
    <div class="center1">
      <img src="../../assets/img/welcom.jpeg" />
    </div>
    <div class="center2">
      <h2>修改读者密码</h2>
      <div class="el-icon-user">
        用户账号 :<el-input
          v-model="id"
          placeholder="请输入你的用户名账号"
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
        新密码 :<el-input
          placeholder="请输入新的密码"
          v-model="password2"
          show-password
        ></el-input>
      </div>
      <el-button type="primary" plain @click="check">立即修改</el-button>
    </div>
  </div>
</template>

<script>
import qs from "qs";
import request from "@/request";
export default {
  name: "checkpassword",
  data() {
    return {
      id: "",
      password: "",
      password2: "",
    };
  },
  methods: {
    check() {
      var data = {
        uid: this.id,
        password: this.password,
        new_password: this.password2,
      };
      const path = "/api/user/checkpassword";
      request.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$router.push("/");
        }
      }); //修改密码
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
  margin-bottom: 10px;
}
.el-button {
  width: 20vw;
  margin-left: 2vw;
}
</style>
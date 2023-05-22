<template>
  <div>
    <el-menu class="el-menu" mode="horizontal">
      <el-submenu index="1">
        <template slot="title">切换语言</template>
        <el-menu-item index="2-1">英语</el-menu-item>
        <el-menu-item index="2-2">法语</el-menu-item>
        <el-menu-item index="2-3">德语</el-menu-item>
        <el-menu-item index="2-3">日语</el-menu-item>
      </el-submenu>
      <el-menu-item index="0">rt-books</el-menu-item>

      <el-menu-item index="2">欢迎光临</el-menu-item>

      <el-menu-item index="5" @click="information">我的信息</el-menu-item>
      <el-menu-item index="4" @click="back">退出登录</el-menu-item>
      <el-menu-item index="3" @click="check">修改密码</el-menu-item>
      <div class="search">
        <el-input v-model="input" placeholder="请输入内容"></el-input>
        <el-button type="primary" plain @click="search">搜索</el-button>
      </div>
    </el-menu>
  </div>
</template>

<script>
import request from "@/request";
export default {
  name: "top",
  data() {
    return {
      input: "",
    };
  },
  methods: {
    information() {
      this.$router.push("/readerinformation");
    },
    back() {
      const path = "/api/user/logout";
      request.delete(path).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$router.push("/");
        }
      }); //退出登录
    },
    check() {
      this.$router.push("/checkpassword");
    },
    search() {
      request.get("/api/user/book/search/" + this.input).then((res) => {
        setTimeout(() => {
          this.$bus.$emit("introduce", res.data);
          this.$bus.$emit("bookid", this.input);
        }, 1000);
        this.$router.push("/introbook");
      }); //给首页发请求拿数据
    },
  },
  mounted() {},
};
</script>

<style scoped >
.el-menu.el-menu--horizontal {
  height: 8vh;
  display: flex;
  justify-content: space-between;
}
el-menu-item {
  width: 20px;
}
.el-input {
  width: 300px;
  margin-top: 10px;
}
.el-button {
  width: 100px;
  margin: auto;
}
</style>
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
    </el-menu>
  </div>
</template>

<script>
import axios from "axios";
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
      const path = "http://localhost:5000/api/user/logout";
      axios.delete(path).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$router.push("/");
        }
      }); //退出登录
    },
    check() {
      this.$router.push("/checkpassword");
    },
  },
  mounted() {
    // this.$bus.$emit("infromation", res.data);
  },
};
</script>

<style scoped >
.el-menu.el-menu--horizontal {
  height: 10vh;
  display: flex;
  justify-content: space-between;
}
.el-menu-item {
  margin-left: 5%;
  font-size: 120%;
}
</style>
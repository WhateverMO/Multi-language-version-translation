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
      <el-submenu index="3">
        <template slot="title">添加图书</template>
        <el-menu-item index="3-1" @click="write">创建新书</el-menu-item>
        <el-menu-item index="3-2" @click="translate">翻译新书</el-menu-item>
      </el-submenu>
      <el-menu-item index="6" @click="author">作者信息</el-menu-item>
      <el-menu-item index="2">rt-books</el-menu-item>
      <el-menu-item index="5">欢迎光临</el-menu-item>
      <el-menu-item index="8" @click="check">修改密码</el-menu-item>
      <el-menu-item index="7" @click="back">退出登录</el-menu-item>
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
    translate() {
      this.$router.push("/choose");
    },
    write() {
      this.$router.push("/kind");
    },
    reader() {
      this.$router.push("/readerinformation");
    },
    author() {
      this.$router.push("/authorinformation");
    },
    check() {
      this.$router.push("/checkpasswordauthor");
    },
    back() {
      const path = "http://localhost:5000/api/author/logout";
      axios.delete(path).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$router.push("/");
        }
      }); //退出登录
    },
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
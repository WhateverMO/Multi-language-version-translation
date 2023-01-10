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
      <el-menu-item index="0" @click="re">rt-books</el-menu-item>
      <el-menu-item index="2">玄幻</el-menu-item>
      <el-menu-item index="3">都市</el-menu-item>
      <el-menu-item index="4">仙侠</el-menu-item>
      <el-menu-item index="5">历史</el-menu-item>
      <el-menu-item index="6">悬疑</el-menu-item>
      <el-menu-item index="7">推理</el-menu-item>
      <el-menu-item index="8">言情</el-menu-item>
      <el-menu-item index="9">更多</el-menu-item>
      <el-input v-model="input" placeholder="请输入内容"></el-input>
      <el-button type="primary" plain>搜索</el-button>
      <el-menu-item index="8" @click="back">退出登录</el-menu-item>
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
    back() {
      const path = "http://localhost:5000/api/user/logout";
      axios.delete(path).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$router.push("/");
        }
      }); //退出登录
    },
    re() {
      this.$router.push("/reader");
    },
  },
};
</script>

<style >
.el-menu.el-menu--horizontal {
  height: 10vh;
  display: flex;
  justify-content: space-between;
}
.el-menu-item {
  margin-left: 5%;
  font-size: 120%;
}
.el-input {
  width: 20vw;
  position: relative;
  margin: auto;
}
.el-button {
  width: 10vw;
  margin: auto;
}
</style>
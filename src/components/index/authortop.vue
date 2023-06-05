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
      <el-menu-item index="9" @click="book">作者作品</el-menu-item>
      <el-menu-item index="6" @click="author">作者信息</el-menu-item>
      <el-menu-item index="2">rt-books</el-menu-item>
      <el-menu-item index="8" @click="check">修改密码</el-menu-item>
      <el-menu-item index="7" @click="back">退出登录</el-menu-item>
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
      const path = "/api/author/logout";
      request.delete(path).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$router.push("/");
        }
      }); //退出登录
    },
    search() {
      request.get("/api/author/book/search/" + this.input).then((res) => {
        console.log(res.data);
        setTimeout(() => {
          this.$bus.$emit("searchbooks", res.data.books);
        }, 1000);
        this.$router.push("/searchbook");
      }); //给首页发请求拿数据
    },
    book() {
      this.$router.push("/authorbook");
    },
  },
};
</script>

<style scoped >
.el-menu.el-menu--horizontal {
  height: 8vh;
  display: flex;
  justify-content: space-between;
}
.el-menu-item {
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
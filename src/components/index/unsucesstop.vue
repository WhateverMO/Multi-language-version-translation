<template>
  <div>
    <el-menu class="el-menu" mode="horizontal">
      <el-submenu index="1">
        <template slot="title">{{ $t("m.changelanguage") }}</template>
        <el-menu-item index="1-1" @click="en">{{
          $t("m.English")
        }}</el-menu-item>
        <el-menu-item index="1-2">{{ $t("m.Korean") }}</el-menu-item>
        <el-menu-item index="1-3">{{ $t("m.German") }}</el-menu-item>
        <el-menu-item index="1-4">{{ $t("m.Japanese") }}</el-menu-item>
        <el-menu-item index="1-5" @click="cn">{{
          $t("m.Chinese")
        }}</el-menu-item>
        <el-menu-item index="1-6">{{ $t("m.Japanese") }}</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">{{ $t("m.registertext") }}</template>
        <el-menu-item index="3-1" @click="enrollauthor">{{
          $t("m.registerauthor")
        }}</el-menu-item>
        <el-menu-item index="3-2" @click="enroll">{{
          $t("m.registerreader")
        }}</el-menu-item>
      </el-submenu>
      <el-submenu index="4">
        <template slot="title">{{ $t("m.logintext") }}</template>
        <el-menu-item index="4-1" @click="loginauthor">{{
          $t("m.loginauthor")
        }}</el-menu-item>
        <el-menu-item index="4-2" @click="loginreader">{{
          $t("m.loginreader")
        }}</el-menu-item>
      </el-submenu>
      <el-menu-item index="0">rt-books</el-menu-item>
      <el-menu-item index="2">{{ $t("m.welcomtext") }}</el-menu-item>
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
    loginreader() {
      this.$router.push("/loginreader");
    },
    loginauthor() {
      this.$router.push("/loginauthor");
    },
    enroll() {
      this.$router.push("/regester");
    },
    enrollauthor() {
      this.$router.push("/regestertranslate");
    },
    en() {
      this.lang = "us";
      this.$i18n.locale = this.lang;
    },
    cn() {
      this.lang = "cn";
      this.$i18n.locale = this.lang;
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
};
</script>

<style scoped >
.el-menu.el-menu--horizontal {
  height: 8vh;
  display: flex;
  justify-content: space-between;
  background-color: #f0f0ed;
}

.el-menu--horizontal > .el-submenu .el-submenu__title {
  color: black;
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
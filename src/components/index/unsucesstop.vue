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
    </el-menu>
  </div>
</template>

<script>
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
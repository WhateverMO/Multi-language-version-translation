<template>
  <div>
    <top />
    <center />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer";
import top from "../../components/index/readertop";
import center from "../../components/index/center";
import request from "@/request";
export default {
  components: {
    top,
    center,
    foot,
  },
  methods: {},
  mounted() {},
};
</script>

<style scoped>
</style>
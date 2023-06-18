<template>
  <div>
    <top />
    <center />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer";
import top from "../../components/index/authortop";
import center from "../../components/index/center";
export default {
  components: {
    top,
    center,
    foot,
  },
};
</script>

<style scoped>
</style>
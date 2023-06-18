<template>
  <div>
    <top />
    <center />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer.vue";
import top from "../../components/index/unsucesstop";
import center from "../../components/index/center";
export default {
  name: "unsucess",
  components: {
    top,
    center,
    foot,
  },
  mounted() {
    sessionStorage.setItem("id", 0);
  },
};
</script>

<style scoped>
</style>
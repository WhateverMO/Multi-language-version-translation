<template>
  <div>
    <top />
    <center />
    <foot />
  </div>
</template>
<script>
import foot from "../../components/login/footer";
import top from "../../components/login/top";
import center from "../../components/login/regestertranslate";
export default {
  components: {
    top,
    foot,
    center,
  },
  data() {
    return {
      ishow: false,
    };
  },
  methods: {},
};
</script>

<style scoped>
</style>
<template>
  <div>
    <top />
    <center />
    <foot />
  </div>
</template>
<script>
import foot from "../../components/login/footer";
import top from "../../components/read/topauthor";
import center from "../../components/login/checkpasswordauthor";
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
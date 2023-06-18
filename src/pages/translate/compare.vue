<template>
  <div>
    <top />
    <compare />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer.vue";
import compare from "@/components/translate/compare.vue";
import top from "@/components/read/top.vue";
export default {
  components: {
    top,
    compare,
    foot,
  },
};
</script>

<style>
</style>
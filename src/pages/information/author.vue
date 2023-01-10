<template>
  <div>
    <top />
    <center />
    <book />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer.vue";
import book from "@/components/information/authorbook.vue";
import center from "@/components/information/authorcenter.vue";
import top from "@/components/read/topauthor.vue";
export default {
  components: {
    top,
    center,
    book,
    foot,
  },
};
</script>

<style>
</style>
<template>
  <div>
    <top />
    <writecenter />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer.vue";
import writecenter from "@/components/addbook/writebook.vue";
import top from "@/components/read/topauthor.vue";
export default {
  components: {
    top,
    writecenter,
    foot,
  },
};
</script>

<style>
</style>
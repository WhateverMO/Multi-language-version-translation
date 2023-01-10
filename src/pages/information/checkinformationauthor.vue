<template>
  <div>
    <top />
    <checkcenter />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer.vue";
import checkcenter from "@/components/information/checkauthor.vue";
import top from "@/components/read/topauthor.vue";
export default {
  components: {
    top,
    checkcenter,
    foot,
  },
};
</script>

<style>
</style>
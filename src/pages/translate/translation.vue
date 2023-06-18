<template>
  <div>
    <top />
    <translatecenter />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer.vue";
import translatecenter from "@/components/translate/mytranslate";
import top from "@/components/read/topauthor.vue";
export default {
  components: {
    top,
    translatecenter,
    foot,
  },
};
</script>

<style>
</style>
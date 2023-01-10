<template>
  <div>
    <top />
    <collect />
    <foot />
  </div>
</template>

<script>
import foot from "@/components/login/footer.vue";
import collect from "@/components/information/collect";
import top from "@/components/read/top.vue";
export default {
  components: {
    top,
    collect,
    foot,
  },
};
</script>

<style>
</style>
<template>
  <div>
    <top />
    <center />
    <foot />
  </div>
</template>
  
  <script>
import foot from "@/components/login/footer.vue";
import center from "@/components/read/searchbook.vue";
import top from "@/components/read/top.vue";
export default {
  components: {
    top,
    center,
    foot,
  },
};
</script>
  
  <style>
</style>
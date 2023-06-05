<template>
  <div>
    <top />
    <attention />
    <foot />
  </div>
</template>
  
  <script>
import foot from "@/components/login/footer.vue";
import attention from "@/components/information/attention";
import top from "@/components/read/top.vue";
export default {
  components: {
    top,
    attention,
    foot,
  },
};
</script>
  
  <style>
</style>
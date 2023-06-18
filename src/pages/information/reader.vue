<template>
  <div>
    <top />
    <center />
    <read />
    <foot />
  </div>
</template>

<script>
import foot from '@/components/login/footer.vue'
import read from '@/components/information/readerread.vue'
import center from '@/components/information/readercenter.vue'
import top from '@/components/read/top.vue'
export default {
  components: {
    top,
    center,
    read,
    foot,
  }
}
</script>

<style>
</style>
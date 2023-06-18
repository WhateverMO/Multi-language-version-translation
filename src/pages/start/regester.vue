<template>
  <div>
    <top />
    <enrollcenter v-if="ishow" />
    <logincenter v-else />
    <foot />
  </div>
</template>
<script>
import logincenter from '../../components/login/logincenter'
import enrollcenter from '../../components/login/enrollcenter'
import foot from '../../components/login/footer'
import top from '../../components/login/top'
export default {
components:{
top,
foot,
enrollcenter,
logincenter
},
    data() {
      return {
        ishow:true,
      }
    },
    methods:{

    }
}
</script>

<style scoped>
</style>
<template>
  <div>
    <top />
       <logincenter />
    <foot />
  </div>
</template>
<script>
import logincenter from '../../components/login/logincenter'
import foot from '../../components/login/footer'
import top from '../../components/login/top'
export default {
components:{
top,
foot,
logincenter
},
    data() {
      return {
      }
    },
    methods:{

    }
}
</script>

<style scoped>
</style>
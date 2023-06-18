<template>
    <div>
        <top />
        <choose />
        <foot />
    </div>
</template>

<script>
import foot from '@/components/login/footer.vue'
import choose from '@/components/translate/choose.vue'
import top from '@/components/read/top.vue'
export default {
    components: {
        top,
        choose,
        foot,
    }
}
</script>

<style>
</style>
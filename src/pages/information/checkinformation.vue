<template>
    <div>
        <top />
        <checkcenter />
        <foot />
    </div>
</template>

<script>
import foot from '@/components/login/footer.vue'
import checkcenter from '@/components/information/check.vue'
import top from '@/components/read/top.vue'
export default {
    components: {
        top,
        checkcenter,
        foot,
    }
}
</script>

<style>
</style>
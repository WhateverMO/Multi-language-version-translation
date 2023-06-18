<template>
    <div>
        <top />
        <kindcenter />
        <foot />
    </div>
</template>

<script>
import foot from '@/components/login/footer.vue'
import kindcenter from '@/components/addbook/kindcenter.vue'
import top from '@/components/read/top.vue'
export default {
    components: {
        top,
        kindcenter,
        foot,
    }
}
</script>

<style>
</style>
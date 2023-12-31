<template>
    <div v-if="alertStatusSuccess === true" style="margin: 0;" class="alert alert-success alert-dismissible fade show" role="alert">
    <strong>Успех!</strong> Задача успешно обработана.
    <button @click="store.closeAlert('success')" type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <div v-if="alertStatusError === true" style="margin: 0;"  class="alert alert-warning alert-dismissible fade show" role="alert">
        <strong>Ошибка!</strong> Произошла ошибка, пожалуйста попробуйте еще раз. 
        <button @click="store.closeAlert('error')" type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
</template>

<script setup>
const props = defineProps({
    alertStatusSuccess: {
        type: Boolean,
        required: true,
    },
    alertStatusError: {
        type: Boolean,
        required: true,
    },
    store: {
        type: Object,
        required: true
    }
})
</script>

<style lang="css" scoped>

</style>
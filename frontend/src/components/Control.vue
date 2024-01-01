<template>
    <div class="control_bar">
        <div class="control_btns">
            <button @click="store.addTableItem()" class="btn btn-warning">Добавить</button>
            <a href="http://localhost:8000/api/v1/docs" class="btn btn-info">API docs</a>
        </div >
    </div>
</template>

<script setup>
const props = defineProps({
    store: {
        type: Object,
        required: true,
    }
});
</script>

<style lang="css" scoped>
.control_btns  {
    display: flex;
    gap: 10px;
}
</style>
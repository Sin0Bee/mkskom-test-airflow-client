<template>   
<div class="table_box">
        <table class="table_main">
            <tr class="table_row_head">
                <th>DAG_ID</th>
                <th>Context</th>
                <th>Interval</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>  

            <hr>
                    
        </table>
    </div>
    <SkeletonItem/>
    <SkeletonItem/>
    <SkeletonItem/>
    <SkeletonItem/>
    <SkeletonItem/>
    <SkeletonItem/>
</template>

<script setup>
import SkeletonItem from './SkeletonItem.vue'

</script>

<style lang="css" scoped>
.table_row_head {
    width: 100%;
    min-height: 50px;
    align-items:center;
    text-align: center;
    display: grid;
    grid-template-columns: repeat(5, 20%);
}

.table_main {
    width: 100%;
    padding: 0 40px;
}

.table_box {
    width: 100%;
    padding: 0 40px;
}
</style>
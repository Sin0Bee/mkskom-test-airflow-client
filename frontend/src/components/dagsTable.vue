<template>
    <div class="table_box">
        <table>
            <tr>
                <th>DAG_ID</th>
                <th>Code</th>
                <th>Interval</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
            <tr class="table_row" v-for="dag in dags">
                <td>{{dag.name}}</td>
                <td>{{dag.context}}</td>
                <td>{{dag.interval}}</td>
                <td>{{dag.status}}</td>
                <td><button @click="getDags()">Update</button><button>Delete</button></td>
            </tr>
            
        </table>
    </div>
</template>

<script setup>

const props = defineProps({
    dags: {
        type: Array,
        required: true
    },
    getDags: {
        type: Function,
        required: true
    }
})
</script>

<style lang="css" scoped>

</style>
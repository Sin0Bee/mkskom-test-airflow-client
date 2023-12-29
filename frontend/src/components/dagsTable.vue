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
            <tr class="table_row" v-for="dag in data.dags">
                <td><strong>{{dag.name}}</strong></td>
                <td><textarea class="table_row_context" name="context">{{dag.context}}</textarea></td>
                <td><input class="table_row_interval" type="number" 
                    :value.number="dag.interval"></td>
                <td>{{dag.status}}</td>
                <td><button @click="dagStore.updateDag(dag.id, {
                    id: dag.id,
                    name: dag.name,
                    context: dag.context,
                    interval: dag.interval,
                    create_at: dag.create_at,
                    update_at: Date.now(),
                    status: dag.status,
                })">Update</button>
                    <button @click="dagStore.delDag(id=dag.id)">Delete</button>
                </td>
            </tr>

            <tr class="table_row" v-if="dagStore.newItem.name === 'New'">                
                <td><input
                    v-model="props.item.name"
                    @input="props.item.name = $event.target.value"
                    class="table_row_context"
                    type="text"
                ></td>
            
                <td><textarea  
                    v-model="props.item.context"
                    @input="props.item.context = $event.target.value"
                    class="table_row_context">
                </textarea></td>
                
                <td><input
                    v-model="props.item.interval"
                    @input="props.item.interval = $event.target.value"  
                    class="table_row_interval" 
                    type="number"></td>
                
                <td>{{dagStore.newItem.status}}</td>

                <td><button @click="addItem">Create</button></td>
                
            </tr>
            
        </table>
    </div>
</template>

<script setup>

const props = defineProps({

    data: {
        type: Array,
        required: true
    },
    dagStore: {
        type: Object,
        required: true
    },
    item: {
        name: 'New',
        context: 'print("Hello World")',
        interval: 0
    },
    addItem: () => {
        this.dagStore.$patch((state) => {
        state.newItem.name = this.item.name;
        state.newItem.context = this.item.context;
        state.newItem.interval = this.item.interval;
        });
        this.dagStore.addDag();
    }
    
})

// const item = {
//     name: 'New',
//     context: 'print("Hello World")',
//     interval: 0
// }

// const addItem = () => {
//     dagStore.$patch((state) => {
//         state.newItem.name = this.item.name;
//         state.newItem.context = this.item.context;
//         state.newItem.interval = this.item.interval;
//     });
//     dagStore.addDag();
// }

</script>

<style lang="css" scoped>


.table_box {
    width: 100%;
    padding: 0 40px;
}
.table_main {
    width: 100%;
    padding: 0 40px;
}
.table_row_head {
    width: 100%;
    min-height: 50px;
    align-items:center;
    display: grid;
    grid-template-columns: repeat(5, 20%);
}
.table_row {
    display: grid;
    grid-template-columns: repeat(5, 20%);
    align-items: center;
    text-align: center;
    width: 100%;
    min-height: 50px;
    margin-top: 5px;
    border-bottom: solid 1px #5f5f5f;
}
.table_row_interval {
    max-width: 90%;
    padding: 0 5px;
    text-align: center;
}
.table_row_context {
    max-width: 90%;
    padding: 5px;
    max-height: 40px;
}
</style>
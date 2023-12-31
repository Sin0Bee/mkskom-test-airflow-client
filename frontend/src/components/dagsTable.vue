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
            <tr class="table_row" v-for="dag in dagStore.data.dags">
                <td>
                    <strong>
                        {{dag.name}}
                    </strong>
                </td>
                <td>
                    <textarea 
                        class="table_row_context" 
                        name="context"
                        :value="dag.context">
                        {{dag.context}}
                    </textarea>
                </td>
                <td>
                    <input 
                        class="table_row_interval" 
                        type="number" 
                        :value.number="dag.interval">
                </td>

                <td v-if="dag.status === true">
                    <span class="table_row_item_status_up">
                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-up-fill" viewBox="0 0 16 16">
                            <path d="m7.247 4.86-4.796 5.481c-.566.647-.106 1.659.753 1.659h9.592a1 1 0 0 0 .753-1.659l-4.796-5.48a1 1 0 0 0-1.506 0z"/>
                        </svg>
                    </span>
                </td>
                <td v-if="dag.status === false">
                    <span class="table_row_item_status_down">
                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-down-fill" viewBox="0 0 16 16">
                            <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
                        </svg>
                    </span>
                </td>

                <td class="table_row_item_actions">
                    <span @click="dagStore.updateDag(dag.id, {
                    id: dag.id,
                    name: dag.name,
                    context: dag.context,
                    interval: dag.interval,
                    create_at: dag.create_at,
                    update_at: Date.now(),
                    status: dag.status,
                })" class="table_row_item_btn_update_dag">
                        <strong>
                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
                            </svg>
                        </strong>
                    </span>
                    <span @click="dagStore.delDag(id=dag.id)" class="table_row_item_btn_delete_dag">
                        <strong>
                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
                                <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
                            </svg>
                        </strong>
                    </span>
                </td>
            </tr>

            <tr class="table_row" v-if="dagStore.actionAddItem">                
                <td><input
                    v-model="dagStore.newItem.name"
                    @input="dagStore.newItem.name = $event.target.value"
                    class="table_row_context"
                    type="text"
                ></td>
            
                <td><textarea  
                    v-model="dagStore.newItem.context"
                    @input="dagStore.newItem.context = $event.target.value"
                    class="table_row_context">
                </textarea></td>
                
                <td><input
                    v-model="dagStore.newItem.interval"
                    @input="dagStore.newItem.interval = $event.target.value"  
                    class="table_row_interval" 
                    type="number"></td>
                
                <td v-if="dagStore.newItem.status === true">
                    <span class="table_row_item_status_up">
                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-up-fill" viewBox="0 0 16 16">
                            <path d="m7.247 4.86-4.796 5.481c-.566.647-.106 1.659.753 1.659h9.592a1 1 0 0 0 .753-1.659l-4.796-5.48a1 1 0 0 0-1.506 0z"/>
                        </svg>
                    </span>
                </td>

                <td v-if="dagStore.newItem.status === false">
                    <span class="table_row_item_status_down">
                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-caret-down-fill" viewBox="0 0 16 16">
                            <path d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
                        </svg>
                    </span>
                </td>

                <td class="table_row_item_actions">
                    <span @click="dagStore.addDag" class="add_new_item">
                        <strong>
                            <svg xmlns="http://www.w3.org/2000/svg" width="29" height="29" fill="currentColor" class="bi bi-check2" viewBox="0 0 16 16">
                                <path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
                            </svg>
                        </strong>
                    </span>
                    <span @click="dagStore.cleanAddTableItem" class="clean_new_item">
                        <strong>
                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
                                <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/>
                            </svg>
                        </strong>
                    </span>
                </td>
                
            </tr>
            
        </table>
    </div>
</template>

<script setup>

const props = defineProps({
    dagStore: {
        type: Object,
        required: true 
    },
    updateItem: {
        type: Object,
        required: false,
        id: 0,
        name: '',
        context: '',
        interval: 0,
        update_at: Date.now(),
        create_at: '',
        status: false
    },
    setUpdateItem: (data) => {
        this.updateItem.id = data.id;
        this.updateItem.name = data.name;
        this.updateItem.context = data.context;
        this.updateItem.interval = data.interval;
        this.updateItem.update_at = data.update_at;
        this.updateItem.create_at = data.create_at;
        this.updateItem.status = data.status;
        return {
            data: this.updateItem
        }
    }
})
</script>

<style lang="css" scoped>
.table_row_item_status_down {
    color: red;
}
.table_row_item_status_up {
    color: green;
}
.table_row_item_btn_delete_dag {
    color: rgb(246, 67, 67);
    cursor: pointer;
}
.table_row_item_btn_delete_dag:hover {
    color: rgb(255, 0, 0);
}
.table_row_item_btn_update_dag {
    color: rgb(255, 125, 32);
    cursor: pointer;
}
.table_row_item_btn_update_dag:hover {
    color: rgb(255, 106, 0);
}
.clean_new_item {
    color: rgb(246, 67, 67);
    cursor: pointer;
}

.clean_new_item:hover {
    color: rgb(248, 0, 0);
}
.add_new_item {
    cursor: pointer;
    color:rgb(44, 112, 15);
}

.add_new_item:hover {
    color:rgb(34, 89, 11);
}

.table_row_item_actions {
    display: flex;
    justify-content: space-around;
    padding: 0 30%;
}

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
    text-align: center;
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
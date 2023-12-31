<script setup>
import dagTable from './components/dagsTable.vue'
import TableSkeleton from './components/TableSkeleton.vue'
import MsgAlert from './components/MsgAlert.vue'
import { useDagsStore } from './store/dagsStore'

const dagStore = useDagsStore();
const loadData = () => {
  dagStore.$patch((state) => {state.loader = true});
  setTimeout(dagStore.getDags, 2000);
}
loadData();


</script>

<template>
  <MsgAlert :store="dagStore" :alertStatusSuccess="dagStore.pushAlertSuccess" :alertStatusError="dagStore.pushAlertError"/>
  <div class="main_container">  

    <header>
      <h1>Список активных DAG файлов</h1>
      <span @click="dagStore.addTableItem" class="add_event">
        
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
          <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
          <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4"/>
        </svg>
      </span>
    </header>
    

    <div v-if="dagStore.loader === true"> <TableSkeleton/></div>
    <div v-if="dagStore.loader === false"><dagTable  :dagStore="dagStore"/></div>
    
  </div>
</template>

<style lang="css">
.add_event {
  color: rgb(30, 78, 9);
}
.main_container {
  background: linear-gradient(#d4d4d4aa, #b3c8e9e8);
  height: 100%;
}

header {
  width: 100%;
  text-align: center;
}


</style>

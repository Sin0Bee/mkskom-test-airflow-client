<script setup>
import dagTable from './components/dagsTable.vue'
import TableSkeleton from './components/TableSkeleton.vue'
import MsgAlert from './components/MsgAlert.vue'
import Control from './components/Control.vue'
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
    <h1>Список активных DAG файлов</h1>
    <div v-if="dagStore.loader === true"> <TableSkeleton/></div>
    <div v-if="dagStore.loader === false"><dagTable  :dagStore="dagStore"/></div>
  </div>
  <div class="control_box">
    <Control :store="dagStore"/>
  </div>
</template>

<style lang="css">
.add_event {
  cursor: pointer;
  color: rgb(30, 78, 9);
}
.add_event:hover {
  color: rgb(54, 132, 21);
}
.main_container {
  height: 100%;
}

@media screen and (min-width: 320px) and (max-width: 1980px) and (max-height: 956px){
  .control_box {
    top: 0px

  }
  .main_container {
    margin-top: 50px;
  }

}

.control_box {
  bottom: 40px;
  position: fixed;
  max-height: 20px;
  width: 100%;
  padding: 10px 40px;
}

body {
  position: relative;
  width: 100%;
  background: linear-gradient(#d4d4d4aa, #b3c8e9e8);
}

h1 {
  width: 100%;
  text-align: center;
}

::-webkit-scrollbar {
  width: 3px;
}
::-webkit-scrollbar-thumb {
  background: linear-gradient(#9c9c9c, #d4d4d4aa);
  border-radius: 6px;
  height: 10px;
}
</style>

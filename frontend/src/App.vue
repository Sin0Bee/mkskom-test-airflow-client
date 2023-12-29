<script setup>
import dagTable from './components/dagsTable.vue'
import { useDagsStore } from './store/dagsStore'

const dagStore = useDagsStore();
dagStore.getDags();

</script>

<template>
  <div class="container">
    <div class="info_box">
      <div class="alert">При операции произошла ошибка.</div>
      <div class="success">Операция прошла успешно.</div>
    </div>
  <div class="main">    
    <header><h1>Список активных DAG файлов</h1><button @click="dagStore.addTableItem" class="add_event">Добавить</button></header>
    
    <dagTable :data="dagStore.data" :dagStore="dagStore"/>
  </div>
  </div>
  
  
</template>

<style lang="css">

.container {
  background: linear-gradient(#d4d4d4aa, #87adece8);
  height: 100%;
}

header {
  width: 100%;
  text-align: center;
  margin: 30px 0px;
}

.info_box {
  top: 0px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 100%;
  height: 40px;
  background: linear-gradient(#d4d4d400);
}

.alert {
  width: 100%;
}

.success {
  width: 100%;
}

</style>

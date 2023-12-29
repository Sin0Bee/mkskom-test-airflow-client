<script setup>
import dagTable from './components/dagsTable.vue'
import { useDagsStore } from './store/dagsStore'

const dagStore = useDagsStore();


</script>

<template>
  <div class="header">
    <h1>Hello World</h1>
    <!-- <dagTable :dags="dagStore.dags" :getDags="dagStore.getDags"/> -->
    <button @click="dagStore.getDags">Update</button>
  </div>
  
</template>

<style scoped>

</style>

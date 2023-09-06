<script setup>
import { RouterLink } from "vue-router";
import BicyclesList from "../components/bicycles/BicyclesList.vue";

// TODO: добавить пагинацию, и фильтр по брендам велосипеда в будущем
const apiUrlBicycleList = "/bicycles/?ordering=-id";
</script>

<template>
  <div class="pt-3">
    <h3>Велосипеды</h3>
    <BicyclesList :apiUrlBicycleList="apiUrlBicycleList" />
  </div>
</template>

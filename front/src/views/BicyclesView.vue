<script setup>
import BicyclesList from "../components/bicycles/BicyclesList.vue";

const bicycleAmount = "?ordering=-id";
// TODO: добавить пагинацию, и фильтр по брендам велосипеда в будущем
</script>

<template>
  <div class="mt-4">
    <BicyclesList :bicycleAmount="bicycleAmount" />
  </div>
</template>

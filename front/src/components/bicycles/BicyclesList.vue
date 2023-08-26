<script setup>
import BicycleCardSmall from "./BicycleCardSmall.vue";
import { ref, onMounted } from "vue";
import axios from "axios";

const props = defineProps({
  bicycleAmount: String,
});

const bicycles = ref([]);

onMounted(() => {
  let apiUrl = "http://127.0.0.1:8000/api/v1/bicycles/";

  if (props.bicycleAmount) {
    apiUrl += props.bicycleAmount;
  } else {
    apiUrl += "?last=5";
  }

  axios
    .get(apiUrl)
    .then((response) => {
      bicycles.value = response.data.results;
      console.log(response.data);
    })
    .catch((error) => {
      console.error("Ошибка при выполнении запроса:", error);
    });
});
</script>

<template>
  <a class="nav-link" href="/bicycles"><h3>Велосипеды</h3></a>
  <div class="row row-cols-1 row-cols-md-3 g-3 mt-2">
    <div class="col" v-for="bike in bicycles" :key="bike.id">
      <BicycleCardSmall :bike="bike" />
    </div>
  </div>
</template>

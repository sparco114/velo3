<script setup>
import BicycleCardSmall from "./BicycleCardSmall.vue";
import { ref, onMounted } from "vue";
// import axios from "axios";
import customAxios from "../../axios.js"


const props = defineProps({
  apiUrlBicycleList: String,
});

const bicycles = ref([]);

onMounted(() => {
  customAxios
    .get(props.apiUrlBicycleList)
    .then((response) => {
      bicycles.value = response.data.results;
      // TODO: убрать на проде
      console.log(response.data);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
      console.error("Ошибка при выполнении запроса:", error);
    });
});
</script>

<template>
  <div v-if="bicycles.length > 0">
    <div class="row row-cols-3 g-3 mt-1">
      <div class="col" v-for="bicycle in bicycles" :key="bicycle.id">
        <BicycleCardSmall :bicycle="bicycle" />
      </div>
    </div>
  </div>
  <div v-else>
    <div class="row justify-content-center row-cols-3 g-3 mt-2">
      <div class="card text-center mb-3 rounded-4">
        <div class="card-body">
          <p class="card-text">
            Не добавлено ни одного велосипеда
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

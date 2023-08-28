<script setup>
import BicycleCardSmall from "./BicycleCardSmall.vue";
import { ref, onMounted } from "vue";
import axios from "axios";

const props = defineProps({
  apiUrlBicycleList: String,
});

const bicycles = ref([]);

onMounted(() => {
  axios
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
  <div class="row row-cols-1 row-cols-md-3 g-3 mt-2">
    <div class="col" v-for="bicycle in bicycles" :key="bicycle.id">
      <BicycleCardSmall :bicycle="bicycle" />
    </div>
  </div>
</template>

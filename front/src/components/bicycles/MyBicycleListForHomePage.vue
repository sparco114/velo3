<script setup>
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import customAxios from "../../axios.js";
import BicycleCardSmall from "./BicycleCardSmall.vue";

// из HomeView
const props = defineProps({
  apiUrlMyBicycleListForHomePage: String,
});

const bicycles = ref([]);

onMounted(() => {
  customAxios
    .get(props.apiUrlMyBicycleListForHomePage)
    .then((response) => {
      bicycles.value = response.data.results;
      console.log(response.data);
    })
    .catch((error) => {
      console.error("Ошибка при выполнении запроса:", error);
    });
});
console.log("bicycles.value---", bicycles.value.length);
// console.log("bicycles---", bicycles);
</script>

<template>
  <div v-if="bicycles.length > 0">
    <div class="row justify-content-center row-cols-3 g-3 mt-2">
      <div class="col" v-for="bicycle in bicycles" :key="bicycle.id">
        <BicycleCardSmall :bicycle="bicycle" />
      </div>
    </div>
  </div>
  <div v-else class="">
    <div class="row justify-content-center row-cols-3 g-3 mt-2">
      <div class="card text-center mb-3 rounded-4">
        <div class="card-body">
          <p class="card-text">Вы пока не добавили велосипед</p>
          <RouterLink
            class="btn btn-l btn-success rounded-4"
            :to="{ name: 'bicycle-create' }"
            >Добавить велосипед</RouterLink
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import LogBookRecordSmall from "./LogBookRecordSmall.vue";

// если потребуется изменить число записей, можно прокинуть количество откуда нужно,
// по умолчанию используется 5 шт
const props = defineProps({
  logBookRecordAmount: String,
  bicycleId: String,
});

const logBookRecords = ref([]);

onMounted(() => {
  let apiUrl = `http://127.0.0.1:8000/api/v1/bicycles/${props.bicycleId}/logbook/`;
  if (props.logBookRecordAmount) {
    apiUrl += props.logBookRecordAmount;
  } else {
    apiUrl += "?last=5";
  }
  // TODO: убрать на проде
  console.log(apiUrl);

  axios
    .get(apiUrl)
    .then((response) => {
      logBookRecords.value = response.data.results;
      // Убрать на проде
      console.log(response.data);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
      console.error("Ошибка при выполнении запроса:", error);
    });
});
</script>

<template>
  <RouterLink class="nav-link" to="#"><h3>Бортжурнал</h3></RouterLink>
  <div v-if="logBookRecords.length > 0">
    <div v-for="record in logBookRecords" :key="record.id">
      <LogBookRecordSmall :record="record" />
    </div>
    <RouterLink class="card mt-3 rounded-4 text-center shadow-sm nav-link full-logbook-button" to="#">
      <div class="card-body fs-5 ">Все записи</div>
    </RouterLink>
  </div>
  <div v-else>Нет записей</div>
</template>


<style>
.full-logbook-button {
    background-color: #19875425;
    outline-width: 10rem;
}
</style>
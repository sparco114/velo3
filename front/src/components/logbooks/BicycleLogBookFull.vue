<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import LogBookRecordMedium from "./LogBookRecordMedium.vue";

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
  <h3>Бортжурнал велосипеда</h3>
  <div v-for="record in logBookRecords" :key="record.id">
    <LogBookRecordMedium :record="record" />
  </div>
</template>

<script setup>
// import axios from "axios";
import customAxios from "../../axios.js"
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import LogBookRecordMedium from "./LogBookRecordMedium.vue";

const props = defineProps({
  logBookRecordAmount: String,
});

const logBookRecords = ref([]);

onMounted(() => {
  let apiUrl = "/logbooks/";

  if (props.logBookRecordAmount) {
    apiUrl += props.logBookRecordAmount;
  } else {
    apiUrl += "?last=5";
  }

  customAxios
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
  <div v-for="record in logBookRecords" :key="record.id">
    <LogBookRecordMedium :record="record" />
  </div>
</template>

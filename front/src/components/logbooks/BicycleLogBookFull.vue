<script setup>
import { ref, onMounted } from "vue";
import customAxios from "../../axios.js";
import LogBookRecordMedium from "./LogBookRecordMedium.vue";
import { DEFAULT_LOGBOOK_RECORDS_AMOUNT } from "../../constants.js";

// из BicycleLogBookFullView
const props = defineProps({
  logBookRecordAmount: String,
  bicycleId: String,
});

const logBookRecords = ref([]);

onMounted(() => {
  let apiUrl = `/bicycles/${props.bicycleId}/logbook/`;

  if (props.logBookRecordAmount) {
    apiUrl += props.logBookRecordAmount;
  } else {
    apiUrl += DEFAULT_LOGBOOK_RECORDS_AMOUNT;
  }

  customAxios
    .get(apiUrl)
    .then((response) => {
      logBookRecords.value = response.data.results;
      console.log(response.data);
    })
    .catch((error) => {
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

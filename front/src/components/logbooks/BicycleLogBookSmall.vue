<script setup>
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import customAxios from "../../axios.js";
import LogBookRecordSmall from "./LogBookRecordSmall.vue";
import { DEFAULT_LOGBOOK_RECORDS_AMOUNT } from "../../constants.js";

// из BicycleDetailView
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
  <div v-if="logBookRecords.length > 0">
    <div v-for="record in logBookRecords" :key="record.id">
      <LogBookRecordSmall :record="record" />
    </div>

    <RouterLink
      class="card mt-3 rounded-4 text-center shadow-sm nav-link full-logbook-button"
      :to="{ name: 'bicycle-logbook-full', params: { id: bicycleId } }"
    >
      <div class="card-body fs-5">Все записи</div>
    </RouterLink>
  </div>

  <div v-else>
    <div class="card text-center my-3 rounded-4">
      <div class="card-body">Нет записей</div>
    </div>
  </div>
</template>

<style>
.full-logbook-button {
  background-color: #19875425;
  outline-width: 10rem;
}
</style>

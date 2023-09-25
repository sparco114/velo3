<script setup>
import { useRoute } from "vue-router";
import BicycleLogBookFull from "../components/logbooks/BicycleLogBookFull.vue";

const bicycleId = useRoute().params.id;
const logBookRecordAmount = "?ordering=-id";
// TODO: добавить пагинацию, и фильтр в будущем
</script>

<template>
  <div class="mt-4">
    <BicycleLogBookFull
      :logBookRecordAmount="logBookRecordAmount"
      :bicycleId="bicycleId"
    />
  </div>
</template>

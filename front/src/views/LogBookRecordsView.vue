<script setup>
import LogBookRecordsList from "../components/logbooks/LogBookRecordsList.vue";

const logBookRecordAmount = "?ordering=-id";
// TODO: добавить пагинацию, и фильтр в будущем
</script>

<template>
  <div class="pt-3">
    <h3>Бортжурналы</h3>
    <LogBookRecordsList :logBookRecordAmount="logBookRecordAmount" />
  </div>
</template>

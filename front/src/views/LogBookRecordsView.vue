<script setup>
import LogBookRecordsList from "../components/logbooks/LogBookRecordsList.vue";

const logBookRecordAmount = "?ordering=-id";
// TODO: добавить пагинацию, и фильтр в будущем
</script>

<template>
  <div class="mt-4">
    <LogBookRecordsList :logBookRecordAmount="logBookRecordAmount" />
  </div>
</template>

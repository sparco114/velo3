<template>
  <!-- <div class="container mt-5 px-custom-feed"> -->
    <UnregistredMainPage />
    <div class="container mt-5">
      <BicyclesList :bicycleAmount="bicycleAmount"/>
    </div>

    <div class="container mt-5">
      <LogBookRecordsList :logBookRecordAmount="logBookRecordAmount"/>
    </div>
  <!-- </div> -->
</template>

<script setup>
import UnregistredMainPage from "../components/common/UnregistredMainPage.vue";
import BicyclesList from "../components/bicycles/BicyclesList.vue";
import LogBookRecordsList from "../components/logbooks/LogBookRecordsList.vue";

const bicycleAmount = "?random=3";
const logBookRecordAmount = "?random=7";
</script>

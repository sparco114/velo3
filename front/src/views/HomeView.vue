<script setup>
import UnregistredMainPage from "../components/common/UnregistredMainPage.vue";
import BicyclesList from "../components/bicycles/BicyclesList.vue";
import LogBookRecordsList from "../components/logbooks/LogBookRecordsList.vue";

const apiUrlBicycleList = "http://127.0.0.1:8000/api/v1/bicycles/?random=3";
const logBookRecordAmount = "?random=7";
</script>

<template>
  <UnregistredMainPage />
  <div class="container mt-5">
    <RouterLink class="nav-link" :to="{ name: 'bicycles-list' }">
      <h3>Примеры других велосипедов</h3>
    </RouterLink>
    <BicyclesList :apiUrlBicycleList="apiUrlBicycleList" />
  </div>

  <div class="container mt-4">
    <RouterLink class="nav-link" :to="{ name: 'logbooks-list' }">
      <h3>Примеры других бортжурналов</h3>
    </RouterLink>
    <LogBookRecordsList :logBookRecordAmount="logBookRecordAmount" />
  </div>
</template>

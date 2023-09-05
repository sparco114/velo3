<script setup>
import UnregistredMainPage from "../components/common/UnregistredMainPage.vue";
import BicyclesList from "../components/bicycles/BicyclesList.vue";
import MyBicycleListForHomePage from "../components/bicycles/MyBicycleListForHomePage.vue";
import LogBookRecordsList from "../components/logbooks/LogBookRecordsList.vue";
import { computed } from "vue";
import { useStore } from "vuex";

const store = useStore();

const logBookRecordAmount = "?random=7";
const apiUrlBicycleList = "http://127.0.0.1:8000/api/v1/bicycles/?random=3";

const userIdInStore = computed(() => store.state.userId);
console.log('userId------from Home - ', userIdInStore)
console.log('store.state.userId------from Home - ', store.state.userId)
let apiUrlMyBicycleListForHomePage = null;
if (userIdInStore) {
  apiUrlMyBicycleListForHomePage = `http://127.0.0.1:8000/api/v1/bicycles/?owner=${userIdInStore.value}`;
}
console.log('apiUrlMyBicycleListForHomePage------- from home-', apiUrlMyBicycleListForHomePage)
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <img
        src="https://webstockreview.net/images/bicycle-clipart-vector-4.png"
        alt="вело"
        class="img-fluid logo-velo"
      />
    </div>
    <div class="row text-center">
      <h1><strong>Бортовой журнал вашего велосипеда</strong></h1>
    </div>

    <div class="row" v-if="userIdInStore">
      <MyBicycleListForHomePage :apiUrlMyBicycleListForHomePage="apiUrlMyBicycleListForHomePage" />
      <!-- ДА -->
    </div>
    <div class="row text-center" v-else>
      <UnregistredMainPage />
      <!-- НЕТ -->
    </div>
  </div>

  <div class="container mt-5">
    <RouterLink class="nav-link" :to="{ name: 'bicycles-list' }">
      <h3>Велосипеды пользователей</h3>
    </RouterLink>
    <BicyclesList :apiUrlBicycleList="apiUrlBicycleList" />
  </div>

  <div class="container mt-4">
    <RouterLink class="nav-link" :to="{ name: 'logbooks-list' }">
      <h3>Бортжурналы пользователей</h3>
    </RouterLink>
    <LogBookRecordsList :logBookRecordAmount="logBookRecordAmount" />
  </div>
</template>

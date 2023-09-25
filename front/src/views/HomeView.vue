<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
import UnregistredMainPage from "../components/common/UnregistredMainPage.vue";
import BicyclesList from "../components/bicycles/BicyclesList.vue";
import MyBicycleListForHomePage from "../components/bicycles/MyBicycleListForHomePage.vue";
import LogBookRecordsList from "../components/logbooks/LogBookRecordsList.vue";

const store = useStore();

const logBookRecordAmount = "?random=7";
const apiUrlBicycleList = "/bicycles/?random=3";

const userIdInStore = computed(() => store.state.userId);

let apiUrlMyBicycleListForHomePage = null;

if (userIdInStore) {
  apiUrlMyBicycleListForHomePage = `/bicycles/?owner=${userIdInStore.value}`;
}
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <!-- TODO: перенести русунко на сервер -->
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
      <MyBicycleListForHomePage
        :apiUrlMyBicycleListForHomePage="apiUrlMyBicycleListForHomePage"
      />
    </div>
    <div class="row text-center" v-else>
      <UnregistredMainPage />
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

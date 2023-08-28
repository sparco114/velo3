<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import BicycleLogBookSmall from "../components/logbooks/BicycleLogBookSmall.vue";
import BicycleOwnerCardSmall from "../components/logbooks/BicycleOwnerCardSmall.vue";
import { RouterLink } from "vue-router";

import BicyclesList from "../components/bicycles/BicyclesList.vue";

const userId = useRoute().params.id;
const apiUrlBicycleList = `http://127.0.0.1:8000/api/v1/bicycles/?owner=${userId}`;

const user = ref([]);

onMounted(() => {
  let apiUrl = `http://127.0.0.1:8000/api/v1/profiles/${userId}/`;

  axios
    .get(apiUrl)
    .then((response) => {
      user.value = response.data;
      // TODO: убрать на проде
      console.log(response.data);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
      console.error("Ошибка при выполнении запроса:", error);
    });
});
</script>

<template>
  <div class="container rounded-4 card shadow-sm mb-3">
    <div class="row card-body">
      <div class="col-2 g-0 avatar-full-profile">
        <img
          src="https://static.toiimg.com/photo/msid-51359359/51359359.jpg"
          class="rounded-circle"
          alt="..."
        />
        <!-- TODO: доработать, чтоб кнопка была только у зарегистрированного пользователя -->
        <!-- <div class="d-flex justify-content-center align-items-center mt-2">
          <button class="btn btn-sm border rounded-5">Редактировать</button>
        </div> -->
      </div>
      <div class="col">
        <div class="card-body ms-2">
          <h5 class="card-title">{{ user.username }}</h5>
          <div class="card-text text-body-secondary">
            {{ user.first_name }} {{ user.last_name }}
          </div>
          <div class="card-text">
            <small class="text-muted">{{ user.city }}</small>
          </div>

          <div class="card-text mt-4">
            This is a wider card with supporting text below as a natural lead-in
            to additional content. This content is a little bit longer.This is a
            wider card with supporting text below as a natural lead-in to
            additional content. This content is a little bit longer.This is a
            wider card with supporting text below as a natural lead-in to
            additional content. This content is a little bit longer.This is a
            wider card with supporting text below as a natural lead-in to
            additional content. This content is a little bit longer.
          </div>
        </div>
      </div>
    </div>
  </div>


  <div class="mt-3">
    <!-- TODO: добавить разделение на активные и бывшие велосипеды -->
    <h3>Велосипеды пользователя</h3>
    <BicyclesList :apiUrlBicycleList="apiUrlBicycleList" />
  </div>


</template>


<style>
.avatar-full-profile {
  width: 8rem;
  height: 8rem;
}

.avatar-full-profile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
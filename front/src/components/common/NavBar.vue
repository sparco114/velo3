<script setup>
import { RouterLink } from "vue-router";
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const redirectToRegistration = () => {
  if (route.name === 'user-registration') {
    router.go(); // Этот вызов обновит текущую страницу
  } else {
    router.push({ name: 'user-registration' });
  }
};
</script>

<template>
  <nav class="navbar fixed-top">
    <div class="container-fluid">
      <strong>
        <RouterLink
          class="navbar-brand navbar-button fs-4 me-5"
          :to="{ name: 'home' }"
        >
          VELO3.RU
        </RouterLink>
      </strong>
      <div class="me-3">
        <RouterLink
          class="nav-link navbar-button fs-5"
          :to="{ name: 'bicycles-list' }"
        >
          Велосипеды
        </RouterLink>
      </div>
      <div class="me-auto">
        <RouterLink
          class="nav-link navbar-button fs-5"
          :to="{ name: 'logbooks-list' }"
        >
          Бортжурналы
        </RouterLink>
      </div>
      <div>
        <button class="btn btn-success border me-2 rounded-4" @click="redirectToRegistration">
          Регистрация
        </button>
        <RouterLink class="btn btn-success border rounded-4" to="#">
          Вход
        </RouterLink>
      </div>
    </div>
  </nav>
</template>

<style>
.navbar {
  background-color: #198754;
}
.navbar-button {
  color: #fff !important;
}
</style>

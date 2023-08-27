<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <nav class="navbar fixed-top">
    <div class="container-fluid">
      <strong>
        <RouterLink class="navbar-brand navbar-button fs-4 me-5"  to="/">
          VELO3.RU
        </RouterLink>
      </strong>
      <div class="me-3">
        <RouterLink class="nav-link navbar-button fs-5" to="/bicycles">
          Велосипеды
        </RouterLink>
      </div>
      <div class="me-auto">
        <RouterLink class="nav-link navbar-button fs-5" to="/logbooks">
          Бортжурналы
        </RouterLink>
      </div>
      <div>
        <RouterLink class="btn btn-success border me-2 rounded-4" to="#">
          Регистрация
        </RouterLink>
        <RouterLink class="btn btn-success border rounded-4" to="#"> Вход </RouterLink>
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
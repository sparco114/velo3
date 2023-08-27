<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="container text-center">
    <div class="row justify-content-center">
      <img
        src="https://webstockreview.net/images/bicycle-clipart-vector-4.png"
        alt="вело"
        class="img-fluid logo-velo"
      />
    </div>
    <div class="row">
      <h1 class="mb-5"><strong>Бортовой журнал вашего велосипеда</strong></h1>
    </div>
    <div class="row">
      <div class="col align-self-center">
        <RouterLink class="btn rounded-4 btn-lg border" to="#">
          Войти
        </RouterLink>
      </div>
    </div>
    <div class="row mt-3">
      <div class="col align-self-center">
        <RouterLink class="btn rounded-4 btn-lg border shadow-sm" to="#">
          Завести бортжурнал
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style>
.logo-velo {
  max-width: 30%;
}
</style>

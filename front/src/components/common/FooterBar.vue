<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <footer class="footer text-center mt-5">
    <div class="container p-2 px-5 d-flex justify-content-center">
      <RouterLink class="nav-link me-3" to="#">О проекте</RouterLink>
      <RouterLink class="nav-link me-3" to="#"> Связь с автором </RouterLink>
      <RouterLink class="nav-link me-3" to="#">
        Политика конфиденциальности
      </RouterLink>
      <RouterLink class="nav-link me-3" to="#">
        Условия использования
      </RouterLink>
    </div>
  </footer>
</template>

<style>
.footer {
  background-color: #1a87541b;
}
</style>

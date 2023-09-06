<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <footer class="footer text-center mt-5">
    <div class="container p-2 px-5 d-flex justify-content-center">
      <RouterLink class="nav-link me-3" to="about-project">
        О проекте
      </RouterLink>
      <RouterLink class="nav-link me-3" to="support">
        Связь с автором
      </RouterLink>
      <RouterLink class="nav-link me-3" to="confidential-policy">
        Политика конфиденциальности
      </RouterLink>
      <RouterLink class="nav-link me-3" to="agreement">
        Пользовательское соглашение
      </RouterLink>
    </div>
  </footer>
</template>

<style>
.footer {
  background-color: #1a87541b;
}
</style>

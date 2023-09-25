<script setup>
import { RouterView } from "vue-router";
import NavBar from "./components/common/NavBar.vue";
import FooterBar from "./components/common/FooterBar.vue";
</script>

<template>
  <header>
    <NavBar />
  </header>

  <div class="container px-custom-feed">
    <RouterView />
  </div>

  <footer>
    <FooterBar />
  </footer>
</template>

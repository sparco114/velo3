<script setup>
import { defineProps } from "vue";
import { RouterLink } from "vue-router";

const props = defineProps({
  bicycle: Object,
});
</script>

<template>
  <div class="card h-100 shadow-sm rounded-4 overflow-hidden">
    <RouterLink
      class="stretched-link"
      :to="{ name: 'bicycle-detail', params: { id: bicycle.id } }"
    />
    <img
      src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg"
      class="card-img-top"
      alt="фото_велосипеда"
    />
    <div class="card-body d-flex flex-column">
      <h5 class="fs-5">
        {{ bicycle.brand }}
        {{ bicycle.model }}
        {{ bicycle.bicycle_name }}
      </h5>
      <p class="card-text text-secondary small mt-auto">{{ bicycle.owner }}</p>
    </div>
  </div>
</template>

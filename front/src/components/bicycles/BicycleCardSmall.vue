<script setup>
import { defineProps } from "vue";
import { RouterLink } from "vue-router";
import {DEFAULT_MAIN_BICYCLE_IMAGE_URL} from "../../constants.js";


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

    <div class="img-wrapper-bike-main-picture">
      <img
        :src="bicycle.pictures || DEFAULT_MAIN_BICYCLE_IMAGE_URL"
        class="card-img-top"
        alt="фото велосипеда"
      />

    </div>

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

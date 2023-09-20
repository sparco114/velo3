<script setup>
import { defineProps } from "vue";
import { RouterLink } from "vue-router";
import { DEFAULT_LOGBOOK_RECORD_IMAGE_URL } from "../../constants.js";

const props = defineProps({
  record: Object,
});
</script>

<template>
  <div class="card shadow-sm mt-3 rounded-4">
    <RouterLink
      class="stretched-link"
      :to="{ name: 'logbook-record-detail', params: { id: record.id } }"
    ></RouterLink>
    <div class="row g-0">
      <div class="col-2 d-flex justify-content-center align-items-center" >


        <img
            :src="record && record.pictures && record.pictures.length > 0 ? record.pictures[0].image : DEFAULT_LOGBOOK_RECORD_IMAGE_URL"
            alt=""
            class="card-img rounded-4 rec-small-picture"
        />



      </div>
      <div class="col-10">
        <div class="card-body">
          <h5 class="card-title mb-0 mt-2">{{ record.header }}</h5>
          <p class="card-text">
            <small class="text-muted">{{ record.category }}</small>
          </p>
          <p class="card-text text-end">
            <small class="text-muted">{{ record.created_at }}</small>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.rec-small-picture {
  width: 80%;
  height: 80%;
  object-fit: cover;
}
</style>

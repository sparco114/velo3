<script setup>
import { DEFAULT_USER_AVATAR_IMAGE } from "../../constants.js";

// из BicycleDetailView
const props = defineProps({
  bicycleOwner: Object,
});
</script>

<template>
  <div class="//card mt-2 rounded-4">
    <div class="row g-2">
      <div class="col-1 d-flex justify-content-center align-items-center">
        <!--TODO: доработать, чтоб на разрешении телефона эта часть с инфо о велосипеде уходила вверх-->
        <div class="avatar-small-card">
          <RouterLink
            v-if="bicycleOwner"
            :to="{ name: 'profile-detail', params: { id: bicycleOwner.id } }"
          >
            <img
              :src="bicycleOwner.avatar || DEFAULT_USER_AVATAR_IMAGE"
              alt="user_avatar"
              class="rounded-circle"
            />
          </RouterLink>
        </div>
      </div>

      <div class="col-11">
        <!-- TODO: Попробовать вынести проверку v-if на уровень выше, чтоб не дублировался код -->
        <div v-if="bicycleOwner" class="ms-2">
          <RouterLink
            class="text-decoration-none text-dark"
            v-if="bicycleOwner"
            :to="{ name: 'profile-detail', params: { id: bicycleOwner.id } }"
          >
            <span class="fs-5">{{ bicycleOwner.username }}</span>
          </RouterLink>
          <br />
          <small class="text-secondary">
            {{ bicycleOwner.city ? bicycleOwner.city : "-" }}
          </small>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.avatar-small-card {
  width: 3rem;
  height: 3rem;
}

.avatar-small-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>

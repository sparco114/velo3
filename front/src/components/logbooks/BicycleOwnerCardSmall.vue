<script setup>
const props = defineProps({
  bicycleOwner: Object,
});
</script>

<template>
  <div class="card mt-2 rounded-4">
    <div class="row g-2">
      <div class="col-1 d-flex justify-content-center align-items-center">
        <!--TODO: доработать, чтоб на разрешении телефона эта часть с инфо о велосипеде уходила вверх-->
        <div class="avatar-small-card">
          <RouterLink
            v-if="bicycleOwner"
            :to="{ name: 'profile-detail', params: { id: bicycleOwner.id } }"
          >
            <img
              src="https://static.toiimg.com/photo/msid-51359359/51359359.jpg"
              alt="user_avatar"
              class="rounded-circle"
            />
          </RouterLink>
        </div>
      </div>
      <div class="col-11">
        <!-- Vue не успевает обнаружить реактивные изменения внутри объекта словаря, 
          поэтому делаем проверку v-if (она может отобразить значение позже, 
          когда оно будет подгружено из базы) -->
        <div v-if="bicycleOwner" class="ms-2">
          <RouterLink
            class="text-decoration-none text-dark"
            v-if="bicycleOwner"
            :to="{ name: 'profile-detail', params: { id: bicycleOwner.id } }"
          >
            <span class="fs-5">{{ bicycleOwner.username }}</span>
          </RouterLink>
          <br />
          <small class="text-secondary">{{
            bicycleOwner.city ? bicycleOwner.city : "-"
          }}</small>
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

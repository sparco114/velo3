<script setup>
import { ref, onMounted, computed } from "vue";
import { useStore } from "vuex";
import { RouterLink, useRoute } from "vue-router";
import customAxios from "../../axios.js";
import BicyclesList from "../bicycles/BicyclesList.vue";
import { DEFAULT_USER_AVATAR_IMAGE } from "../../constants.js";

const store = useStore();
const route = useRoute();

// TODO: в одних местах получаю user id из route, а в других из vuex store,
// выяснить как ой вариант опитимальней (в этом случае требуется из обоих мест)
const userIdFromRoute = computed(() => route.params.id);
const userIdFromStore = computed(() => store.state.userId);

const apiUrlBicycleList = `/bicycles/?owner=${userIdFromRoute.value}`;
const user = ref([]);

onMounted(() => {
  let apiUrl = `/profiles/${userIdFromRoute.value}/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      user.value = response.data;

      // TODO: !! разобраться с безопасностью, т.к. приходится отображать это через v-html= в template
      // if (user.value.velouser_profile) {
      user.value.velouser_profile.about = response.data.velouser_profile.about
        ? response.data.velouser_profile.about.replace(/\n/g, "<br>")
        : "";
      // }
      console.log(response.data);
    })
    .catch((error) => {
      console.error("Ошибка при выполнении запроса:", error);
    });
});
</script>

<template>
  <div class="container rounded-4 card shadow-sm mb-3">
    <div class="row card-body">
      <div class="col-2 g-0 avatar-full-profile">
        <img
          :src="user.avatar || DEFAULT_USER_AVATAR_IMAGE"
          class="rounded-circle"
          alt="avatar"
        />

        <div
          v-if="userIdFromRoute == userIdFromStore"
          class="d-flex justify-content-center align-items-center mt-2"
        >
          <!-- TODO: подумать откуда лучше брать id, из userIdFromRoute или из userIdFromStore -->
          <RouterLink
            class="btn btn-sm btn-outline-secondary border rounded-5"
            :to="{ name: 'profile-edit' }"
          >
            Редактировать
          </RouterLink>
        </div>
      </div>

      <div class="col">
        <div class="card-body ms-2">
          <h5 class="card-title">{{ user.username }}</h5>
          <div class="card-text text-body-secondary" v-if="user.first_name">
            {{ user.first_name }} {{ user.last_name }}
          </div>
          <div class="card-text text-body-secondary text-muted" v-else>
            Имя: -
          </div>

          <div class="card-text" v-if="user.city">
            <small class="text-muted">{{ user.city }}</small>
          </div>
          <div class="card-text" v-else>
            <small class="text-muted">Город: - </small>
          </div>

          <div v-if="user.velouser_profile">
            <div class="card-text">
              <div v-if="user.velouser_profile.phone">
                <small class="text-muted">
                  Контакты: {{ user.velouser_profile.phone }}
                </small>
              </div>
              <div class="card-text" v-else>
                <small class="text-muted">Контакты: - </small>
              </div>
            </div>

            <div class="card-text mt-4">
              <div v-if="user.velouser_profile.about">
                <div v-html="user.velouser_profile.about"></div>
              </div>
              <div class="card-text text-body-secondary text-muted" v-else>
                О себе: -
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="mt-3">
    <!-- TODO: добавить разделение на активные и бывшие велосипеды -->
    <div class="row">
      <h3 class="col">Велосипеды пользователя</h3>
      <div class="col text-end">
        <RouterLink
          class="btn btn-sm btn-success rounded-5"
          v-if="userIdFromRoute == userIdFromStore"
          :to="{ name: 'bicycle-create' }"
        >
          Добавить велосипед
        </RouterLink>
      </div>
    </div>

    <BicyclesList :apiUrlBicycleList="apiUrlBicycleList" />
  </div>
</template>

<style>
.avatar-full-profile {
  width: 8rem;
  height: 8rem;
}

.avatar-full-profile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>

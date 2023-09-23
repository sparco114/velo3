<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
import { RouterLink, useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const store = useStore();

// TODO: подумать, нужно ли это обновление страницы
/* Обновление страницы при нажатии Регистриция, если пользователь уже находится на странице регистрации, требуется для быстрой очистки полей формы, если позлователю нужно ввести другие данные */
const redirectToRegistration = () => {
  if (route.name === "user-registration") {
    router.go(); // Этот вызов обновит текущую страницу
  } else {
    router.push({ name: "user-registration" });
  }
};

/* Проверка авторизации, для отображения на странице разной информации в зависимости от этого */
const isLoggedIn = computed(() => store.state.authToken !== null);

const logoutUser = () => {
  store.commit("clearAuthToken"); // Удаление токена из "vue store" и из "local storage"
  store.commit("clearUserId"); // Удаление "user id" из "vue store" и из "local storage"
  console.log("clearAuthToken-out", store.state.authToken);
  console.log("clearUserId-out", store.state.userId);
  router.push({ name: "user-login" });
};
</script>

<template>
  <nav class="navbar fixed-top">
    <div class="container-fluid">
      <strong>
        <RouterLink
          class="navbar-brand navbar-button fs-4 me-5"
          :to="{ name: 'home' }"
        >
          logo
        </RouterLink>
      </strong>

      <div class="me-3">
        <RouterLink
          class="nav-link navbar-button fs-5"
          :to="{ name: 'bicycles-list' }"
        >
          Велосипеды
        </RouterLink>
      </div>

      <div class="me-auto">
        <RouterLink
          class="nav-link navbar-button fs-5"
          :to="{ name: 'logbooks-list' }"
        >
          Бортжурналы
        </RouterLink>
      </div>

      <div v-if="!isLoggedIn">
        <button
          class="btn btn-success border me-2 rounded-4"
          @click="redirectToRegistration"
        >
          Регистрация
        </button>
        <RouterLink
          class="btn btn-success border rounded-4"
          :to="{ name: 'user-login' }"
        >
          Вход
        </RouterLink>
      </div>

      <div v-else>
        <RouterLink
          v-if="store.state.userId"
          class="btn btn-success border rounded-4 me-3"
          :to="{ name: 'profile-detail', params: { id: store.state.userId } }"
        >
          Мой профиль
          <!-- {{ store.state.userId }} -->
        </RouterLink>

        <button class="btn text-white rounded-4" @click="logoutUser">
          Выйти
        </button>
      </div>
    </div>
  </nav>
</template>

<style>
.navbar {
  background-color: #198754;
}

.navbar-button {
  color: #fff !important;
}
</style>

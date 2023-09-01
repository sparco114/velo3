<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();

const username = ref("");
const email = ref("");
const password = ref("");
const re_password = ref("");

// TODO: !! добавить асинхронность и обработку ошибок
// TODO: !! добавить валидацию полей
// Получение заполненных регистрационных данных пользователя и отправка их с post на бэк
const registerUser = () => {
  const userData = {
    username: username.value,
    email: email.value,
    password: password.value,
    re_password: re_password.value,
  };

  axios
    .post("http://127.0.0.1:8000/api/v1/djoser_auth/users/", userData)
    .then((response) => {
      console.log("Пользователь зарегистрирован:", response.data);
      // TODO: !! либо сделать автопереход на страницу лоигна, 
      // либо реализовать автоматический лоигн и уже после этого переход на страницу пользователя 
      router.push({ name: "profile-detail", params: { id: response.data.id } });
    })
    .catch((error) => {
      // console.error("Ошибка при регистрации:", error);
      console.error("Ошибка при регистрации----:", error.response.data);
    });
};
</script>

<template>
  <div class="ms-1 mb-2 fs-3 text-center">Регистрация</div>
  <div class="card mb-4 rounded-4">
    <form class="card-body ms-4 pb-4" @submit.prevent="registerUser">
      <div class="row align-items-center mb-3">
        <div class="">
          <label for="username" class="col-form-label">Никнейм:</label>
        </div>
        <div class="col-4">
          <input
            v-model="username"
            type="text"
            id="username"
            class="form-control"
            aria-describedby="passwordHelpInline"
            required
          />
        </div>
        <div class="col-auto">
          <span id="passwordHelpInline" class="form-text">
            Только латинские буквы и цифры.
          </span>
        </div>
      </div>

      <div class="row align-items-center mb-3">
        <div class="">
          <label for="email" class="col-form-label">Email:</label>
        </div>
        <div class="col-4">
          <input
            v-model="email"
            type="email"
            id="email"
            class="form-control"
            aria-describedby="passwordHelpInline"
            required
          />
        </div>
      </div>

      <div class="row align-items-center mb-3">
        <div class="">
          <label for="password" class="col-form-label">Пароль:</label>
        </div>
        <div class="col-4">
          <input
            v-model="password"
            type="password"
            id="password"
            class="form-control"
            aria-describedby="passwordHelpInline"
            required
          />
        </div>
        <div class="col-auto">
          <span id="passwordHelpInline" class="form-text">
            Длина 6 - 20 символов.
          </span>
        </div>
      </div>

      <div class="row align-items-center mb-5">
        <div class="">
          <label for="re_password" class="col-form-label">
            Подтверждение пароля:
          </label>
        </div>
        <div class="col-4">
          <input
            v-model="re_password"
            type="password"
            id="re_password"
            class="form-control"
            aria-describedby="passwordHelpInline"
            required
          />
        </div>
      </div>

      <div class="d-flex justify-content-center">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Подтвердить
        </button>
      </div>
    </form>
  </div>
</template>

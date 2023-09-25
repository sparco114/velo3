<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import customAxios from "../axios.js";

const router = useRouter();
const store = useStore();

const username = ref("");
const password = ref("");
const credentialsErrorLogInMessage = ref("");
const otherErrorLogInMessage = ref("");

// TODO: попробовал использовать асинхронность, можно в будущем добавть ее в остальные места
// проверить все ли ошибки отлавливаются при входе/выходе пользователя (не только в этой функции)
const loginUser = async () => {
  try {
    const response = await customAxios.post("/djoser_token/token/login/", {
      username: username.value,
      password: password.value,
    });
    const token = response.data.auth_token; // Предполагается, что сервер возвращает токен в поле 'auth_token'
    const userId = response.data.user_id; // Предполагается, что сервер возвращает токен в поле 'user_id'
    credentialsErrorLogInMessage.value = ""; // Очищаем сообщение
    otherErrorLogInMessage.value = ""; // Очищаем сообщение

    if (token && userId) {
      store.commit("setAuthTokenFromApi", token); // добавляем токен в vue store и local storage
      store.commit("setUserIdFromFromApi", userId); // добавляем id в vue store и local storage
    } else {
      console.log("Токен или user_id не получен в ответе", response.data);
    }

    // router.push({ name: "home" });

    /* TODO: Проконтролировать, всегда ли сейчас при нажатии Войти происходит редирект на
    страницу пользователя без ошибок. Если будут ошибки можно раскомментировать редирект на home */
    router.push({ name: "profile-detail", params: { id: userId } });
  } catch (error) {
    store.commit("clearAuthToken"); // удаляем токен из vue store и local storage
    store.commit("clearUserId"); // удаляем id из vue store и local storage
    // console.error("Ошибка входа:", error.response.data.non_field_errors);

    /* TODO: Можно добавить проверку логина и пароля как в UserRegistrationView,
    чтоб не отправлять на сервер лишних запросов */

    if (
      error.response.data.non_field_errors ==
      "Unable to log in with provided credentials."
    ) {
      otherErrorLogInMessage.value = "Неверное имя пользователя или пароль";
    } else {
      otherErrorLogInMessage.value =
        "Ошибка при входе. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
    }
  }
};
</script>

<template>
  <div class="ms-1 mb-2 fs-3 text-center">Вход</div>
  <div class="card mb-4 rounded-4">
    <form class="card-body ms-4 pb-4" @submit.prevent="loginUser">
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
      </div>

      <div class="d-flex justify-content-center">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Войти
        </button>
      </div>
      <div class="d-flex justify-content-center">
        <div class="text-danger mt-2">
          {{ otherErrorLogInMessage }}
        </div>
      </div>
    </form>
  </div>
</template>

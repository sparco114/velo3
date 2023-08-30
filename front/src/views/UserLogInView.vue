<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useStore } from 'vuex';


const router = useRouter();
const store = useStore();

const username = ref("");
const password = ref("");


// TODO: попробовал использовать асинхронность, можно в будущем добавть ее в остальные места
// проверить все ли ошибки отлавливаются при входе/выходе пользователя (не только в этой функции)
const loginUser = async () => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/v1/djoser_token/token/login/",
      {
        username: username.value,
        password: password.value,
      }
    );
    const token = response.data.auth_token; // Предполагается, что сервер возвращает токен в поле 'auth_token'
    if (token) {
      store.commit('setAuthToken', token);
    }
    else {
      console.log("Токен не получен в ответе", response.data)
    }
    
    // TODO: на проде удалить.
    console.log("Вход выполнен:", response.data);
    router.push({ name: "home"});
  } catch (error) {
    localStorage.removeItem('authToken')
    // TODO: на проде отправлять в лог
    console.error("Ошибка входа:", error);
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
    </form>
  </div>
</template>

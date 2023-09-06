<script setup>
import { ref, onMounted, computed } from "vue";
import customAxios from "../axios.js"

// import axios from "axios";
// import { RouterLink } from "vue-router";
// import { useStore } from "vuex";
// import { useRoute } from "vue-router";

// const store = useStore();
// const route = useRoute();

// TODO: в одних местах получаю user id из route, а в других из vuex store,
// выяснить как ой вариант опитимальней (в этом случае требуется из обоих мест)
// const userIdFromRoute = computed(() => route.params.id);
// const userIdFromStore = computed(() => store.state.userId);

// const apiUrlBicycleList = `http://127.0.0.1:8000/api/v1/bicycles/?owner=${userIdFromRoute.value}`;
const user = ref([]);

onMounted(() => {
  let apiUrl = `/my/profile/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      user.value = response.data;
      // TODO: убрать на проде
      console.log("response.data------", response.data);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
      //   console.error("Ошибка при выполнении запроса:", error);
    });
});

const successMessage = ref(""); // Сообщение об успешном сохранении
const errorMessage = ref(""); // Сообщение об ошибке

const updateUserProfile = () => {
  const apiUrl = "/my/profile/";
  successMessage.value = "";
  errorMessage.value = "";

  customAxios
    .patch(apiUrl, user.value) // Отправляем данные пользователя
    .then((response) => {
      console.log("Данные успешно сохранены:", response.data);
      successMessage.value = "Данные успешно сохранены";
      // TODO: Можно добавить обновление состояния приложения в хранилище Vuex, если это необходимо
    })
    .catch((error) => {
      console.error("Ошибка при сохранении данных:", error);
      errorMessage.value =
        "Произошла ошибка при сохранении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения об ошибке пользователю
    });
};
</script>

<template>
  <!-- TODO: проверить классы, если ненужные для бутстрап, то удалить, тк форма скопирована с drf -->
  <!-- TODO: !! настроить проверку всех полей при заполнении, а смену почты с подтверждением -->

  <div class="ms-1 mb-2 fs-3 text-center">Редактирование профиля</div>

  <div class="card mt-3">
    <div class="card-body">
      <h5 class="card-title">{{ user.username }}</h5>
      <fieldset>
        <div class="form-group">
        </div>

        <div class="form-group mt-3">
          <label class="col-sm-2 control-label"> Имя </label>

          <div class="col-sm-10">
            <input
              name="first_name"
              class="form-control"
              type="text"
              v-model="user.first_name"
            />
          </div>
        </div>

        <div class="form-group mt-3">
          <label class="col-sm-2 control-label"> Фамилия </label>

          <div class="col-sm-10">
            <input
              name="last_name"
              class="form-control"
              type="text"
              v-model="user.last_name"
            />
          </div>
        </div>

        <div class="form-group mt-3">
          <label class="col-sm-2 control-label"> Email </label>

          <div class="col-sm-10">
            <input
              name="email"
              class="form-control"
              type="email"
              v-model="user.email"
              disabled
              readonly
            />
          </div>
        </div>

        <div class="form-group mt-3">
          <label class="col-sm-2 control-label"> Город </label>

          <div class="col-sm-10">
            <input
              name="city"
              class="form-control"
              type="text"
              v-model="user.city"
            />
          </div>
        </div>

        <div class="form-group mt-3">
          <label class="col-sm-2 control-label"> Аватар </label>

          <div class="col-sm-10">
            <input name="avatar" type="file" value="" />
          </div>
        </div>

        <div v-if="user.velouser_profile">
          <div class="form-group mt-3">
            <label class="col-sm-2 control-label"> Пол </label>

            <div class="col-sm-10">
              <select
                class="form-control"
                name="velouser_profile.sex"
                v-model="user.velouser_profile.sex"
              >
                <option value="null">-</option>
                <option value="М">М</option>
                <option value="Ж">Ж</option>
                <option value="не указан">не указан</option>
              </select>
            </div>
          </div>

          <div class="form-group mt-3">
            <label class="col-sm-2 control-label"> Дата рождения </label>

            <div class="col-sm-10">
              <input
                name="velouser_profile.birthday"
                class="form-control"
                type="date"
                v-model="user.velouser_profile.birthday"
              />
            </div>
          </div>

          <div class="form-group mt-3">
            <label class="col-sm-2 control-label"> Контакты </label>

            <div class="col-sm-10">
              <input
                name="velouser_profile.phone"
                class="form-control"
                type="text"
                v-model="user.velouser_profile.phone"
              />
            </div>
          </div>

          <div class="form-group mt-3">
            <label class="col-sm-2 control-label"> О себе </label>

            <div class="col-sm-10">
              <textarea
                name="velouser_profile.about"
                class="form-control"
                v-model="user.velouser_profile.about"
              >
              </textarea>
            </div>
          </div>
        </div>

        <div class="form-actions mt-3 row">
          <div class="col-2">
            <button
              class="btn btn-success rounded-4"
              title="Make a PUT request on the My Velo User resource"
              @click="updateUserProfile"
            >
              Сохранить
            </button>
          </div>

          <span v-if="successMessage" class="text-success col-10 ml-2 my-2">{{
            successMessage
          }}</span>
          <span v-if="errorMessage" class="text-danger col-10 ml-2">{{
            errorMessage
          }}</span>
        </div>
      </fieldset>
      <!-- </form> -->
    </div>
  </div>
</template>

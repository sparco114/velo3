<script setup>
import { ref, onMounted, computed } from "vue";
import customAxios from "../axios.js";

const user = ref([]);

/* TODO: Раздел "О себе" нужно доработать, чтоб при отображении сохранялось исходное форматирование, 
т.е. отображать с абзацы с новых строк */
onMounted(() => {
  let apiUrl = `/my/profile/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      user.value = response.data;
      console.log("response.data-", response.data);
    })
    .catch((error) => {
      console.error("Ошибка при выполнении запроса:", error);
    });
});

const successMessage = ref(""); // Сообщение об успешном сохранении
const errorMessage = ref(""); // Сообщение об ошибке
const avatarUploadMessage = ref(""); // Информационное сообщение при имзенении фото

// TODO: Можно переписать функционал как в LogBookRecordCreateView (сохранять фото как отдельную модель на бэке)
// Добавляем файл в запрос
const handleAvatarUpload = (event) => {
  const file = event.target.files[0];
  const maxSize = 1 * 1024 * 1024; // 1 МБ в байтах
  if (file && file.size > maxSize) {
    alert("Файл слишком большой. Максимальный размер файла: 1 МБ.");
    event.target.value = ""; // Очистить выбранный файл
    return;
  }
  avatarUploadMessage.value = `Изображение "${file.name}" будет загружено после СОХРАНЕНИЯ ИЗМЕНЕНИЙ`;
  user.value.avatar = file;
};

// Создаем временную переменную для отправки данных на сервер
const userForUpdate = computed(() => {
  const updatedUser = { ...user.value };

  updatedUser["velouser_profile.sex"] = updatedUser.velouser_profile.sex;
  updatedUser["velouser_profile.birthday"] =
    updatedUser.velouser_profile.birthday;
  updatedUser["velouser_profile.phone"] = updatedUser.velouser_profile.phone;
  updatedUser["velouser_profile.about"] = updatedUser.velouser_profile.about;

  // Если прикреплено новое фото - оставляем updatedBicycle как есть
  if (updatedUser.avatar instanceof File) {
  }
  // Если новое фото не прикреплено - удаляем инфо из updatedBicycle, чтоб в запросе оно не отправлялось и действующее фото не изменялось
  else {
    console.log("сработал - delete updatedUser.avatar");
    delete updatedUser.avatar;
  }
  return updatedUser;
});

const clearAvatar = () => {
  userForUpdate.value.avatar = "";
  avatarUploadMessage.value =
    "Изображение будет удалено при СОХРАНЕНИИ ИЗМЕНЕНИЙ";
};

const updateUserProfile = () => {
  const apiUrl = "/my/profile/";

  successMessage.value = "";
  errorMessage.value = "";
  avatarUploadMessage.value = "";

  customAxios
    .put(apiUrl, userForUpdate.value, {
      headers: { "Content-Type": "multipart/form-data" },
    })
    .then((response) => {
      successMessage.value = "Данные успешно сохранены";
      user.value.avatar = response.data.avatar;
      console.log("Данные успешно сохранены:", response.data);
    })
    .catch((error) => {
      errorMessage.value =
        "Произошла ошибка при сохранении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      console.error("Ошибка при сохранении данных:", error);
      // TODO: Можно добавить вывод сообщения о причине ошибки пользователю
    });
};
</script>

<!-- Дата рождения и Пол нигде не указываются на сайте, в будущем необходимо добваить -->
<!-- TODO: проверить классы, если ненужные для бутстрап, то удалить, тк форма скопирована с drf -->
<!-- TODO: !! настроить проверку всех полей при заполнении, а смену почты с подтверждением -->
<template>
  <div class="ms-1 mb-2 fs-3 text-center">Редактирование профиля</div>

  <div class="card mt-3">
    <form
      class="card-body"
      enctype="multipart/form-data"
      @submit.prevent="updateUserProfile"
    >
      <h5 class="card-title">{{ user.username }}</h5>
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
              rows="6"
              v-model="user.velouser_profile.about"
            >
            </textarea>
          </div>
        </div>
      </div>

      <div v-if="avatarUploadMessage">
        <div class="row align-items-center mt-2" v-if="user.avatar">
          <div class="col alert alert-primary rounded-4">
            {{ avatarUploadMessage }}
          </div>
          <div class="col">
            <button
              @click.prevent="clearAvatar"
              class="btn btn-sm btn-outline-danger rounded-4"
            >
              Удалить фото
            </button>
          </div>
        </div>
      </div>

      <div v-else>
        <div class="row align-items-center mt-2" v-if="user.avatar">
          <div class="col-3">
            <div class="avatar-full-profile">
              <img :src="user.avatar" alt="" class="rounded-circle border" />
            </div>
          </div>
          <div class="col">
            <button
              @click.prevent="clearAvatar"
              class="btn btn-sm btn-outline-danger rounded-4"
            >
              Удалить фото
            </button>
          </div>
        </div>

        <div class="row align-items-center mt-2" v-else>
          <label>
            Фотография
            <span class="text-secondary">
              (максимальный размер файла: 1 МБ.)
            </span>
          </label>
          <div class="col">
            <input
              name="avatar_pict"
              type="file"
              accept="image/*"
              @change="handleAvatarUpload"
            />
          </div>
        </div>
      </div>

      <div class="form-actions mt-3 row">
        <div class="col d-flex justify-content-center">
          <button class="btn btn-success w-50 rounded-5" type="submit">
            Сохранить изменения
          </button>
        </div>
        <div class="text-center mt-2">
          <span v-if="successMessage" class="text-success col-10 ml-2 my-2">{{
            successMessage
          }}</span>
          <span v-if="errorMessage" class="text-danger col-10 ml-2">{{
            errorMessage
          }}</span>
        </div>
      </div>
    </form>
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

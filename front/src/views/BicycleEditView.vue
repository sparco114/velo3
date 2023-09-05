<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import router from "../router";

const store = useStore();
const bikeId = useRoute().params.id;

const userIdFromStore = computed(() => store.state.userId);

const bicycle = ref({});

onMounted(() => {
  let apiUrl = `http://127.0.0.1:8000/api/v1/my/bicycles/${bikeId}/`;

  axios
    .get(apiUrl)
    .then((response) => {
      bicycle.value = response.data;
      // Перезаписываем значение about, заменяя в нем переносы на <br>,
      // а пробелы на &nbsp; чтоб отображать на странице корректное форматирование
      // TODO: можно подумать над другим способом, чтоб не перезаписывать внутри запроса
      // TODO: !! разобраться с безопасностью, т.е. приходится отображать это через v-html= в template
      bicycle.value.about = response.data.about; //.replace(/\n/g, "<br>") //.replace(/ /g, "&nbsp;");
      // TODO: убрать на проде
      console.log(response.data);
      console.log(bicycle.value);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
      console.error("Ошибка при выполнении запроса:", error);
    });
});

const successBicycleUpdateMessage = ref(""); // Сообщение об успешном сохранении
const errorBicycleUpdateMessage = ref(""); // Сообщение об ошибке

const updateMyBicycle = () => {
  const apiUrl = `http://127.0.0.1:8000/api/v1/my/bicycles/${bikeId}/`;
  successBicycleUpdateMessage.value = "";
  errorBicycleUpdateMessage.value = "";

  console.log("newBicycle-----перед отправкой", bicycle.value);
  axios
    .patch(apiUrl, bicycle.value)
    .then((response) => {
      console.log("Информация о велосипеде успешно обновлена:", response.data);
      // TODO: добавить редирект на страницу пользователя
      successBicycleUpdateMessage.value =
        "Информация о велосипеде успешно обновлена";
      // TODO: Можно добавить обновление состояния приложения в хранилище Vuex, если это необходимо
    })
    .catch((error) => {
      console.error("Ошибка при создании велосипеда:", error);
      errorBicycleUpdateMessage.value =
        "Произошла ошибка при сохранении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения об ошибке пользователю
    });
};

function confirmDelete() {
  if (confirm("Вы уверены, что хотите удалить велосипед?")) {
    deleteMyBicycle();
  }
}

const deleteMyBicycle = () => {
  const apiUrl = `http://127.0.0.1:8000/api/v1/my/bicycles/${bikeId}/`;
  successBicycleUpdateMessage.value = "";
  errorBicycleUpdateMessage.value = "";

  //   console.log("newBicycle-----перед отправкой", bicycle.value);
  axios
    .delete(apiUrl)
    .then((response) => {
      console.log("Информация о велосипеде успешно удалена:", response.data);
      // TODO: добавить редирект на страницу пользователя
      //   successBicycleUpdateMessage.value =
      //     "Информация о велосипеде успешно удалена";
      router.push({
        name: "profile-detail",
        params: { id: userIdFromStore.value },
      });
      // TODO: Можно добавить обновление состояния приложения в хранилище Vuex, если это необходимо
    })
    .catch((error) => {
      console.error("Ошибка при удалении велосипеда:", error);
      errorBicycleUpdateMessage.value =
        "Произошла ошибка при удалении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения об ошибке пользователю
    });
};
</script>

<template>
  <div class="ms-1 mb-2 fs-3 text-center">Редактировать велосипед</div>
  <div class="card mb-4 rounded-4">
    <form class="card-body ms-4 pb-4" @submit.prevent="updateMyBicycle">
      <div class="row align-items-center">
        <label for="bicycleName">Никнейм велосипеда</label>
        <div class="col-5">
          <input
            v-model="bicycle.bicycle_name"
            type="text"
            id="bicycleName"
            class="form-control"
            required
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="brand">Бренд</label>
        <div class="col-5">
          <input
            v-model="bicycle.brand"
            type="text"
            id="brand"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="model">Модель</label>
        <div class="col-5">
          <input
            v-model="bicycle.model"
            type="text"
            id="model"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="releaseYear">Год выпуска</label>
        <div class="col-5">
          <input
            v-model="bicycle.release_year"
            type="number"
            id="releaseYear"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="wheelSize">Размер колес</label>
        <div class="col-5">
          <select
            class="form-control"
            id="wheelSize"
            v-model="bicycle.wheel_size"
          >
            TODO: не срабатывает selected
            <option value="" selected="">--------</option>
            <option value="10">10</option>
            <option value="12">12</option>
            <option value="14">14</option>
            <option value="16">16</option>
            <option value="18">18</option>
            <option value="20">20</option>
            <option value="24">24</option>
            <option value="26">26</option>
            <option value="27.5">27.5</option>
            <option value="28">28</option>
            <option value="29">29</option>
            <option value="36">36</option>
          </select>
        </div>
      </div>

      <div class="row align-items-center">
        <label for="frameMaterial">Материал рамы</label>
        <div class="col-5">
          <input
            v-model="bicycle.frame_material"
            type="text"
            id="frameMaterial"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="purchaseYear">Год покупки</label>
        <div class="col-5">
          <input
            v-model="bicycle.purchase_year"
            type="number"
            id="purchaseYear"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="price">Цена, руб.</label>
        <div class="col-5">
          <input
            v-model="bicycle.price"
            type="number"
            id="price"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center my-2">
        <div class="col-5">
          <div class="form-check">
            <input
              class="form-check-input"
              type="checkbox"
              v-model="bicycle.is_former"
              id="isFormer"
            />
            <label class="form-check-label" for="isFormer">
              Это мой бывший велосипед
            </label>
          </div>
        </div>
      </div>

      <div class="row align-items-center">
        <label for="about">О велосипеде</label>
        <div class="col">
          <textarea
            v-model="bicycle.about"
            id="about"
            class="form-control"
            rows="10"
          />
        </div>
      </div>

      <div class="row align-items-center mt-2">
        <label>Фотография</label>
        <div class="col">
          <input name="pictures" type="file" value="" />
        </div>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Сохранить изменения
        </button>
      </div>
      <div class="text-center mt-2">
        <!-- <span
          v-if="successBicycleUpdateMessage"
          class="text-success col-10 ml-2 my-2"
          >{{ successBicycleUpdateMessage }}</span
        > -->
        <span
          v-if="errorBicycleUpdateMessage"
          class="text-danger col-10 ml-2"
          >{{ errorBicycleUpdateMessage }}</span
        >
      </div>
    </form>
  </div>
  <div class="row">
    <div class="col text-end">
      <button
        @click="confirmDelete"
        class="btn btn-sm rounded-5 border btn-outline-danger"
      >
        удалить велосипед
      </button>
    </div>
  </div>
</template>

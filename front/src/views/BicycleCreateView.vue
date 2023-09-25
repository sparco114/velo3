<script setup>
import { ref } from "vue";
import router from "../router";
import customAxios from "../axios.js";

const bicycle = ref({});

const errorBicycleCreateMessage = ref(""); // Сообщение об ошибке

// TODO: Можно переписать функционал как в LogBookRecordCreateView (сохранять фото как отдельную модель на бэке)
// Добавляем файл в запрос
const handleBicycleCreatePictureUpload = (event) => {
  const file = event.target.files[0]; // Берем первый файл (т.к. выбирать на странице можно только один)
  const maxSize = 3 * 1024 * 1024; // 3 МБ в байтах
  if (file && file.size > maxSize) {
    alert("Файл слишком большой. Максимальный размер файла: 3 МБ.");
    event.target.value = ""; // Очистить выбранный файл
    return;
  }
  bicycle.value.pictures = file;
};

const createNewBicycle = () => {
  const apiUrl = "/my/bicycles/create/";

  errorBicycleCreateMessage.value = "";

  customAxios
    .post(apiUrl, bicycle.value, {
      headers: { "Content-Type": "multipart/form-data" }, //указываем из-за отправки изображения
    })
    .then((response) => {
      router.push({ name: "bicycle-detail", params: { id: response.data.id } });
      console.log("Велосипед успешно создан:", response.data);
    })
    .catch((error) => {
      errorBicycleCreateMessage.value =
        "Произошла ошибка при создании велосипеда. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      console.error("Ошибка при создании велосипеда:", error);
    });
};
</script>

<template>
  <div class="ms-1 mb-2 fs-3 text-center">Новый велосипед</div>
  <div class="card mb-4 rounded-4">
    <form class="card-body ms-4 pb-4" @submit.prevent="createNewBicycle">
      <div class="row align-items-center">
        <label for="bicycle_name">Никнейм велосипеда</label>
        <div class="col-5">
          <input
            v-model="bicycle.bicycle_name"
            type="text"
            id="bicycle_name"
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
        <label for="release_year">Год выпуска</label>
        <div class="col-5">
          <input
            v-model="bicycle.release_year"
            type="number"
            id="release_year"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="wheel_size">Размер колес</label>
        <div class="col-5">
          <!-- TODO: не срабатывает selected -->
          <select
            class="form-control"
            id="wheel_size"
            v-model="bicycle.wheel_size"
          >
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
        <label for="frame_material">Материал рамы</label>
        <div class="col-5">
          <input
            v-model="bicycle.frame_material"
            type="text"
            id="frame_material"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="purchase_year">Год покупки</label>
        <div class="col-5">
          <input
            v-model="bicycle.purchase_year"
            type="number"
            id="purchase_year"
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
              id="is_former"
            />
            <label class="form-check-label" for="is_former">
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
            rows="8"
          />
        </div>
      </div>

      <div class="row align-items-center mt-2">
        <label>
          Фотография
          <span class="text-secondary">
            (максимальный размер файла: 3 МБ.)
          </span>
        </label>
        <div class="col">
          <input
            name="pictures"
            type="file"
            accept="image/*"
            @change="handleBicycleCreatePictureUpload"
          />
        </div>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Создать велосипед
        </button>
      </div>
      <div class="text-center mt-2">
        <span v-if="errorBicycleCreateMessage" class="text-danger col-10 ml-2">
          {{ errorBicycleCreateMessage }}
        </span>
      </div>
    </form>
  </div>
</template>

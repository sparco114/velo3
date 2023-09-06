<script setup>
import { ref, onMounted, computed } from "vue";
// import axios from "axios";
import router from "../router";
import customAxios from "../axios.js"


const bicycle = ref({});

// const successBicycleCreateMessage = ref(""); // Сообщение об успешном сохранении
const errorBicycleCreateMessage = ref(""); // Сообщение об ошибке

const createNewBicycle = () => {
  const apiUrl = "/my/bicycles/create/";
  // successBicycleCreateMessage.value = "";
  errorBicycleCreateMessage.value = "";

  console.log("newBicycle-----перед отправкой", bicycle.value);
  customAxios
    .post(apiUrl, bicycle.value)
    .then((response) => {
      console.log("Велосипед успешно создан:", response.data);
      // successBicycleCreateMessage.value = "Велосипед успешно создан";
      router.push({ name: "bicycle-detail", params: { id: response.data.id } });
      // TODO: Можно добавить обновление состояния приложения в хранилище Vuex, если это необходимо
    })
    .catch((error) => {
      console.error("Ошибка при создании велосипеда:", error);
      errorBicycleCreateMessage.value =
        "Произошла ошибка при создании велосипеда. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения об ошибке пользователю
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
          <select
            class="form-control"
            id="wheel_size"
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
        <label>Фотография</label>
        <div class="col">
          <input name="pictures" type="file" value="" />
        </div>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Создать велосипед
        </button>
      </div>
      <div class="text-center mt-2">
        <!-- <span
          v-if="successBicycleCreateMessage"
          class="text-success col-10 ml-2 my-2"
          >{{ successBicycleCreateMessage }}</span
        > -->
        <span
          v-if="errorBicycleCreateMessage"
          class="text-danger col-10 ml-2"
          >{{ errorBicycleCreateMessage }}</span
        >
      </div>
    </form>
  </div>
</template>

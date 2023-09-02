<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";

const bicycleName = ref();
const brand = ref();
const model = ref();
const releaseYear = ref();
const wheelSize = ref();
const frameMaterial = ref();
const purchaseYear = ref();
const price = ref();
const isFormer = ref();
const about = ref();

const successBicycleCreateMessage = ref(""); // Сообщение об успешном сохранении
const errorBicycleCreateMessage = ref(""); // Сообщение об ошибке

const createNewBicycle = () => {
  const apiUrl = "http://127.0.0.1:8000/api/v1/my/bicycles/create/";
  successBicycleCreateMessage.value = "";
  errorBicycleCreateMessage.value = "";

  const newBicycle = {
    bicycle_name: bicycleName.value,
    brand: brand.value,
    model: model.value,
    release_year: releaseYear.value,
    wheel_size: wheelSize.value,
    frame_material: frameMaterial.value,
    purchase_year: purchaseYear.value,
    price: price.value,
    is_former: isFormer.value,
    about: about.value,
    // pictures: null,
  };

  console.log('newBicycle-----перед отправкой', newBicycle)
  axios
    .post(apiUrl, newBicycle)
    .then((response) => {
      console.log("Велосипед успешно создан:", response.data);
      // TODO: добавить редирект на страницу пользователя
      successBicycleCreateMessage.value = "Велосипед успешно создан";
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
        <label for="bicycleName">Никнейм велосипеда</label>
        <div class="col-5">
          <input
            v-model="bicycleName"
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
          <input v-model="brand" type="text" id="brand" class="form-control" />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="model">Модель</label>
        <div class="col-5">
          <input v-model="model" type="text" id="model" class="form-control" />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="releaseYear">Год выпуска</label>
        <div class="col-5">
          <input
            v-model="releaseYear"
            type="number"
            id="releaseYear"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="wheelSize">Размер колес</label>
        <div class="col-5">
          <select class="form-control" id="wheelSize" v-model="wheelSize">
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
            v-model="frameMaterial"
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
            v-model="purchaseYear"
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
            v-model="price"
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
              v-model="isFormer"
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
          <textarea v-model="about" id="about" class="form-control" />
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
        <span
          v-if="successBicycleCreateMessage"
          class="text-success col-10 ml-2 my-2"
          >{{ successBicycleCreateMessage }}</span
        >
        <span
          v-if="errorBicycleCreateMessage"
          class="text-danger col-10 ml-2"
          >{{ errorBicycleCreateMessage }}</span
        >
      </div>
    </form>
  </div>
</template>

<style>
/* <!-- TODO: проверить классы, если ненужные для бутстрап, то удалить, тк форма взята с drf -->

  <div class="ms-1 mb-2 fs-3 text-center">Новый велосипед</div>
  <div class="card mb-4 rounded-4" >
    <!-- TODO: разобраться до конца как работает @submit.prevent, и, возможно переписать -->
    <form class="card-body ms-4 pb-4" @submit.prevent="createNewBicycle">
      <div class="form-group">
        <label for="bicycle_name" class="col-form-label"> Имя велосипеда </label>

        <div class="col-9">
          <input
            id="bicycle_name"
            class="form-control"
            type="text"
            v-model="bicycleName"
            required
          />
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-2 control-label"> Брэнд </label>

        <div class="col-sm-10">
          <input name="brand" class="form-control" type="text" value="" />
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-2 control-label"> Модель </label>

        <div class="col-sm-10">
          <input name="model" class="form-control" type="text" value="" />
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label"> Год выпуска </label>

        <div class="col-sm-9">
          <input
            name="release_year"
            class="form-control"
            type="number"
            value=""
          />
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label"> Размер колес </label>

        <div class="col-sm-9">
          <select class="form-control" name="wheel_size">
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

      <div class="form-group">
        <label class="col-sm-3 control-label"> Материал рамы </label>

        <div class="col-sm-9">
          <input
            name="frame_material"
            class="form-control"
            type="text"
            value=""
          />
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-3 control-label"> Год покупки </label>

        <div class="col-sm-9">
          <input
            name="purchase_year"
            class="form-control"
            type="number"
            value=""
          />
        </div>
      </div>

      <div class="form-group">
        <label class="col-sm-2 control-label"> Цена </label>

        <div class="col-sm-10">
          <input name="price" class="form-control" type="number" value="" />
        </div>
      </div>

      <!-- TODO: временно убрал, если поле в дальнейшем не потребуется, 
          то нужно убрать его так же в апи в соответствующем эндпойнте -->
      <!-- <div class="form-group horizontal-checkbox">
            <label class="col-sm-2 control-label"> Is former </label>

            <div class="col-sm-10">
              <input type="checkbox" name="is_former" value="true" />
            </div>
          </div> -->

      <div class="form-group">
        <label class="col-sm-2 control-label"> О велосипеде </label>

        <div class="col-sm-10">
          <textarea name="about" class="form-control"></textarea>
        </div>
      </div>

      <div class="form-group mt-2">
        <label class="col-sm-2 control-label"> Фотография </label>

        <div class="col-sm-10">
          <input name="pictures" type="file" value="" />
        </div>
      </div>

      <div class="form-actions mt-3 d-flex justify-content-center">
        <button
          class="btn btn-success rounded-4"
          title=""
          data-original-title="Make a POST request on the My Bicycle Create resource"
    
        >
          Создать велосипед
        </button>
      </div>
    </form>
  </div> */
</style>

<script setup>
import { ref, onMounted, computed } from "vue";
// import axios from "axios";
import router from "../router";
import { useRoute } from "vue-router";
import customAxios from "../axios.js"


const bikeId = useRoute().params.id;

const logBookRecord = ref({});
const formData = new FormData();

// const successRecordCreateMessage = ref(""); // Сообщение об успешном сохранении
const errorRecordCreateMessage = ref(""); // Сообщение об ошибке



// TODO: !! Разобраться нужно ли переписать функционал следующим образом:
//  - добавить апи для загрузки фото
//  - добавить кнопку Загрузить фото в этой форме, которая будет загружать фото, а в ответ получать
//    адрес этого фото, и записывать его в поле pictures объекта logBookRecord.
// Добавляем файл в запрос


const handleRecordPicturesUpload = (event) => {
  const files = event.target.files;
  const maxSize = 3 * 1024 * 1024; // 3 МБ в байтах
  const selectedFiles = [];
  if (files && files.size > maxSize) {
    alert("Файл слишком большой. Максимальный размер файла: 3 МБ.");
    event.target.value = ""; // Очистить выбранный файл
    return;
  }
    for (let i = 0; i < files.length; i++) {
    if (files[i].size > maxSize) {
      alert(`Файл ${files[i].name} слишком большой. Максимальный размер файла: 3 МБ.`);
    } else {
      selectedFiles.push(files[i]);
    }
  }

  for (let i = 0; i < selectedFiles.length; i++) {
    formData.append(`picturesss[${i}]`, selectedFiles[i]);
  }
  


    // for (const file of selectedFiles) {
    // formData.append('pictures', file);
  // }
  formData.append("header", logBookRecord.value.header);
  formData.append("text", logBookRecord.value.text);
 
  };




// const handleRecordPicturesUpload = (event) => {
//   const files = event.target.files[0];
//   const maxSize = 3 * 1024 * 1024; // 3 МБ в байтах
//   const selectedFiles = [];



//   if (files && files.size > maxSize) {
//     alert("Файл слишком большой. Максимальный размер файла: 3 МБ.");
//     event.target.value = ""; // Очистить выбранный файл
//     return;
//   }
   

//   logBookRecord.value.pictures = files;
// };




const createNewLogBookRecord = () => {
  const apiUrl = `/bicycles/${bikeId}/logbook/create/`;
  //   successRecordCreateMessage.value = "";
  errorRecordCreateMessage.value = "";




  console.log('formData + pictures  ------перед отправкой', console.table(Object.fromEntries(formData)) )
  // console.log("newBicycle-----перед отправкой", logBookRecord.value);
  customAxios
    .post(apiUrl, formData, {
      headers: { "Content-Type": "multipart/form-data" }, //указываем только из-за отправки изображения
    })
    .then((response) => {
      console.log("Запись успешно создана:", response.data);
      // successBicycleCreateMessage.value = "Велосипед успешно создан";
      router.push({
        name: "logbook-record-detail",
        params: { id: response.data.id },
      });
      // TODO: Можно добавить обновление состояния приложения в хранилище Vuex, если это необходимо
    })
    .catch((error) => {
      console.error("Ошибка при создании записи:", error);
      errorRecordCreateMessage.value =
        "Произошла ошибка при создании записи. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения об ошибке пользователю
    });
};
</script>

<template>
  <div class="ms-1 mb-2 fs-3 text-center">Новая запись</div>
  <div class="card mb-4 rounded-4">
    <form class="card-body ms-4 pb-4" @submit.prevent="createNewLogBookRecord">
      <div class="row align-items-center">
        <label for="header">Заголовок</label>
        <div class="col">
          <input
            v-model="logBookRecord.header"
            type="text"
            id="header"
            class="form-control"
            required
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="text">Текст</label>
        <div class="col">
          <textarea
            v-model="logBookRecord.text"
            type="text"
            id="text"
            class="form-control"
            rows="10"
            required
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="mileage">Пробег</label>
        <div class="col-5">
          <input
            v-model="logBookRecord.mileage"
            type="number"
            id="mileage"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="cost">Стоимость</label>
        <div class="col-5">
          <input
            v-model="logBookRecord.cost"
            type="number"
            id="cost"
            class="form-control"
          />
        </div>
      </div>

      <div class="row align-items-center">
        <label for="category">Категория</label>
        <div class="col-5">
          <select
            class="form-control"
            id="category"
            v-model="logBookRecord.category"
          >
            TODO: не срабатывает selected
            <option value="" selected="">не указано</option>
            <optgroup label="---">
              <option value="руль">руль</option>
              <option value="вилка">вилка</option>
              <option value="система переклчения">система переклчения</option>
              <option value="звезды">звезды</option>
              <option value="тормоза">тормоза</option>
              <option value="седло">седло</option>
              <option value="педали">педали</option>
              <option value="обода">обода</option>
              <option value="покрышки">покрышки</option>
              <option value="аксессуары">аксессуары</option>
              <option value="рама">рама</option>
              <option value="поломка">поломка</option>
              <option value="плановое ТО">плановое ТО</option>
              <option value="другое">другое</option>
            </optgroup>

            <optgroup label="---">
              <option value="гонка">гонка</option>
              <option value="тренировка">тренировка</option>
              <option value="ПВД">ПВД</option>
              <option value="прогулка">прогулка</option>
            </optgroup>
            <optgroup label="---">
              <option value="покупка велосипеда">покупка велосипеда</option>
              <option value="продажа велосипеда">продажа велосипеда</option>
            </optgroup>
          </select>
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
            id="pictures"
            type="file"
            accept="image/*"
            @change="handleRecordPicturesUpload"
            multiple
          />
        </div>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Создать запись
        </button>
      </div>
      <div class="text-center mt-2">
        <!-- <span
          v-if="successBicycleCreateMessage"
          class="text-success col-10 ml-2 my-2"
          >{{ successBicycleCreateMessage }}</span
        > -->
        <span v-if="errorRecordCreateMessage" class="text-danger col-10 ml-2">{{
          errorRecordCreateMessage
        }}</span>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import router from "../router";
import { useRoute } from "vue-router";
import customAxios from "../axios.js";

const bikeId = useRoute().params.id;

const logBookRecord = ref({});
const formData = new FormData();

const errorRecordCreateMessage = ref(""); // Сообщение об ошибке

const selectedFileNames = ref([]); // Имена выбранных файлов для отображения их на странице

// Добавление файлов в запрос
const handleRecordPicturesUpload = (event) => {
  const files = event.target.files;
  const maxSize = 3 * 1024 * 1024; // 3 МБ в байтах
  const selectedFiles = [];

  if (files && files.length > 6) {
    alert("Максимальное количество файлов - 6 шт.");
    event.target.value = ""; // Очистить выбранный файл
    return;
  }

  // TODO: некорректно отображается количество выбранных файлов, если некоторые из них превышают максимальный размер
  for (let i = 0; i < files.length; i++) {
    if (files[i].size > maxSize) {
      alert(
        `Файл "${files[i].name}" не будет загружен, так как слишком большой. Максимальный размер файла: 3 МБ.`
      );
      // return;
    } else {
      selectedFiles.push(files[i]);
    }
  }

  selectedFileNames.value = []; // Очистить список предыдущих имен файлов

  // Если есть выбранные файлы, получаем их имена и добавляем в selectedFileNames
  if (selectedFiles.length > 0) {
    for (let i = 0; i < selectedFiles.length; i++) {
      selectedFileNames.value.push(selectedFiles[i].name);
    }
  }

  //  TODO: слить вместе с заполнением selectedFileNames, чтоб не дублировался код
  // Добавляем файлы в formData для отправки запроса
  for (let i = 0; i < selectedFiles.length; i++) {
    formData.append(`picturess[${i}]`, selectedFiles[i]);
  }
};

const createNewLogBookRecord = () => {
  const apiUrl = `/bicycles/${bikeId}/logbook/create/`;
  errorRecordCreateMessage.value = "";

  formData.append("header", logBookRecord.value.header);
  formData.append("text", logBookRecord.value.text);
  formData.append(
    "mileage",
    logBookRecord.value.mileage ? logBookRecord.value.mileage : ""
  );
  formData.append(
    "cost",
    logBookRecord.value.cost ? logBookRecord.value.cost : ""
  );
  formData.append(
    "category",
    logBookRecord.value.category ? logBookRecord.value.category : ""
  );

  // console.log(
  //   "formData - перед отправкой",
  //   console.table(Object.fromEntries(formData))
  // );
  customAxios
    .post(apiUrl, formData, {
      headers: { "Content-Type": "multipart/form-data" }, //указываем из-за отправки изображения
    })
    .then((response) => {
      console.log("Запись успешно создана:", response.data);
      router.push({
        name: "logbook-record-detail",
        params: { id: response.data.id },
      });
    })
    .catch((error) => {
      console.error("Ошибка при создании записи:", error);
      errorRecordCreateMessage.value =
        "Произошла ошибка при создании записи. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения о причине ошибки пользователю
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
          <!-- TODO: не срабатывает selected -->
          <select
            class="form-control"
            id="category"
            v-model="logBookRecord.category"
          >
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
        <label>Фотография</label>
        <span class="text-secondary">
          (Максимальное количество файлов - 6 шт.)
        </span>
        <div class="text-secondary mb-2">
          (Максимальный размер каждого файла: 3 МБ.)
        </div>
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

      <div v-if="selectedFileNames.length > 0">
        Выбранные файлы:
        <ul>
          <li v-for="(fileName, index) in selectedFileNames" :key="index">
            {{ fileName }}
          </li>
        </ul>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Создать запись
        </button>
      </div>

      <div class="text-center mt-2">
        <span v-if="errorRecordCreateMessage" class="text-danger col-10 ml-2">
          {{ errorRecordCreateMessage }}
        </span>
      </div>
    </form>
  </div>
</template>

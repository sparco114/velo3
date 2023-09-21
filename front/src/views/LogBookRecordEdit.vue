<script setup>
import { ref, onMounted, computed } from "vue";
// import axios from "axios";
import customAxios from "../axios.js";
import router from "../router";
import { useRoute } from "vue-router";

const logBookRecordId = useRoute().params.id;

const logBookRecord = ref({});
const formData = new FormData();


onMounted(() => {
  let apiUrl = `/logbooks/${logBookRecordId}/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      logBookRecord.value = response.data;
      // TODO: убрать на проде

      //   record.value.text = response.data.text
      //     ? response.data.text //.replace(/\n/g, "<br>") //.replace(/ /g, "&nbsp;")
      //     : "";

      console.log(response.data);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
      console.error("Ошибка при выполнении запроса:", error);
    });
});


const selectedFileNames = ref([]);


const handleRecordPicturesUpload = (event) => {
  const files = event.target.files;
  const maxSize = 3 * 1024 * 1024; // 3 МБ в байтах
  const selectedFiles = [];

  const amountUploadedPictures = logBookRecord.value.pictures.length

  if (files && (files.length + amountUploadedPictures) > 6) {
    alert("Общее количество файлов в статье не может первышать 6 шт.");
    event.target.value = ""; // Очистить выбранный файл
    return;
  }

  // if (files && files.size > maxSize) {
  //   alert("Файл слишком большой. Максимальный размер файла: 3 МБ.");
  //   event.target.value = ""; // Очистить выбранный файл
  //   return;
  // }
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

  // Очистить список предыдущих имен файлов
  selectedFileNames.value = [];


  // Если есть выбранные файлы, получаем их имена
  if (selectedFiles.length > 0) {
    for (let i = 0; i < selectedFiles.length; i++) {
      selectedFileNames.value.push(selectedFiles[i].name);
    }
  }
//  TODO: слить вместе с заполнением selectedFileNames, чтоб не дублировался код
  for (let i = 0; i < selectedFiles.length; i++) {
    formData.append(`picturess[${i}]`, selectedFiles[i]);
  }
};












// const successRecordCreateMessage = ref(""); // Сообщение об успешном сохранении
const errorRecordUpdateMessage = ref(""); // Сообщение об ошибке

const updateLogBookRecord = () => {
  const apiUrl = `/logbooks/${logBookRecordId}/update/`;
  //   successRecordCreateMessage.value = "";
  errorRecordUpdateMessage.value = "";



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




    console.log('table(Object.fromEntries(formData)', Object.fromEntries(formData));
  // console.log("newBicycle-----перед отправкой", logBookRecord.value);
  customAxios
    .patch(apiUrl, formData, {
      headers: { "Content-Type": "multipart/form-data" }, //указываем только из-за отправки изображения
    })
    .then((response) => {
      console.log("Запись успешно обновлена:", response.data);
      // successBicycleCreateMessage.value = "Велосипед успешно создан";
      router.push({
        name: "logbook-record-detail",
        params: { id: response.data.id },
      });
      // TODO: Можно добавить обновление состояния приложения в хранилище Vuex, если это необходимо
    })
    .catch((error) => {
      console.error("Информация в записи успешно обновлена:", error);
      errorRecordUpdateMessage.value =
        "Произошла ошибка при сохранении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения об ошибке пользователю
    });
};

function confirmDeleteRecord() {
  if (confirm("Вы уверены, что хотите удалить запись?")) {
    deleteLogBookRecord();
  }
}

const deleteLogBookRecord = () => {
  const apiUrl = `/logbooks/${logBookRecordId}/update/`;
  //   successBicycleUpdateMessage.value = "";
  errorRecordUpdateMessage.value = "";

  //   console.log("newBicycle-----перед отправкой", bicycle.value);
  customAxios
    .delete(apiUrl)
    .then((response) => {
      console.log("Запист успешно удалена:", response.data);
      // TODO: добавить редирект на страницу пользователя
      //   successBicycleUpdateMessage.value =
      //     "Информация о велосипеде успешно удалена";
      router.push({
        name: "bicycle-logbook-full",
        params: { id: logBookRecord.value.bicycle.id },
      });
      // TODO: Можно добавить обновление состояния приложения в хранилище Vuex, если это необходимо
    })
    .catch((error) => {
      console.error("Ошибка при удалении записи:", error);
      errorRecordUpdateMessage.value =
        "Произошла ошибка при удалении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения об ошибке пользователю
    });
};
</script>

<template>
  <div class="ms-1 mb-2 fs-3 text-center">Редактирование записи</div>
  <div class="card mb-4 rounded-4">
    <form class="card-body ms-4 pb-4" @submit.prevent="updateLogBookRecord">
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
            type="file" 
            value="" 
            accept="image/*" 
            @change="handleRecordPicturesUpload" 
            multiple/>
        </div>

        <div
          class="row align-items-center mt-2"
          v-if="logBookRecord.pictures && logBookRecord.pictures.length > 0"
          v-for="picture in logBookRecord.pictures"
        >
          <div class="col-3">
            <div class="img-wrapper-bike-main-picture">
              <img :src="picture.image" alt="" class="rounded-3 border" />
            </div>
          </div>
          <div class="col">
            <button
              @click.prevent="clearPicture"
              class="btn btn-sm btn-outline-danger rounded-4"
            >
              Удалить фото
            </button>
          </div>
        </div>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Сохранить изменения
        </button>
      </div>
      <div class="text-center mt-2">
        <!-- <span
          v-if="successBicycleCreateMessage"
          class="text-success col-10 ml-2 my-2"
          >{{ successBicycleCreateMessage }}</span
        > -->
        <span v-if="errorRecordUpdateMessage" class="text-danger col-10 ml-2">{{
          errorRecordUpdateMessage
        }}</span>
      </div>
    </form>
  </div>
  <div class="row">
    <div class="col text-end">
      <button
        @click="confirmDeleteRecord"
        class="btn btn-sm rounded-5 border btn-outline-danger"
      >
        удалить запись
      </button>
    </div>
  </div>
</template>

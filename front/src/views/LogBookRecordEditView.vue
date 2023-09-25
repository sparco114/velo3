<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import customAxios from "../axios.js";
import router from "../router";

const logBookRecordId = useRoute().params.id;

const logBookRecord = ref({});
const formData = new FormData();

onMounted(() => {
  let apiUrl = `/logbooks/${logBookRecordId}/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      logBookRecord.value = response.data;
      console.log(response.data);
    })
    .catch((error) => {
      console.error("Ошибка при выполнении запроса:", error);
    });
});

const errorPictureDeleteMessage = ref("");

// Запрос на удаление фотографии с сервера
const deletePicture = (pictureId) => {
  const apiUrl = `/pictures/${pictureId}/delete/`;

  customAxios
    .delete(apiUrl)
    .then((response) => {
      /* Удаляем информацию о фото из logBookRecord 
      путем формирования нового аналогичного массива, но без указанной фотографии */
      logBookRecord.value.pictures = logBookRecord.value.pictures.filter(
        (picture) => picture.id !== pictureId
      );
      console.log(`Фотография с id ${pictureId} успешно удалена`);
    })
    .catch((error) => {
      errorPictureDeleteMessage.value =
        "Произошла ошибка при удалении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      console.error(`Ошибка при удалении фотографии с id ${pictureId}:`, error);
    });
};

const selectedFileNames = ref([]); // Имена выбранных файлов для отображения их на странице

// Добавление файлов в запрос
const handleRecordPicturesUpload = (event) => {
  const files = event.target.files;
  const maxSize = 3 * 1024 * 1024; // 3 МБ в байтах
  const selectedFiles = [];

  const amountUploadedPictures = logBookRecord.value.pictures.length; // Количество выбранных файлов

  if (files && files.length + amountUploadedPictures > 6) {
    alert("Общее количество файлов в статье не может первышать 6 шт.");
    event.target.value = ""; // Очистить список выбранных файлов
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

const errorRecordUpdateMessage = ref(""); // Сообщение об ошибке

const updateLogBookRecord = () => {
  const apiUrl = `/logbooks/${logBookRecordId}/update/`;

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

  // console.log(
  //   "table(Object.fromEntries(formData)--------",
  //   Object.fromEntries(formData)
  // );

  customAxios
    .put(apiUrl, formData, {
      headers: { "Content-Type": "multipart/form-data" }, //указываем из-за отправки изображения
    })
    .then((response) => {
      router.push({
        name: "logbook-record-detail",
        params: { id: response.data.id },
      });
      console.log("Запись успешно обновлена:", response.data);
    })
    .catch((error) => {
      errorRecordUpdateMessage.value =
        "Произошла ошибка при сохранении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      console.error("Ошибка при обновлении записи:", error);
      // TODO: Можно добавить вывод сообщения о причине ошибки пользователю
    });
};

function confirmDeleteRecord() {
  if (confirm("Вы уверены, что хотите удалить запись?")) {
    deleteLogBookRecord();
  }
}

const deleteLogBookRecord = () => {
  const apiUrl = `/logbooks/${logBookRecordId}/update/`;

  errorRecordUpdateMessage.value = "";

  customAxios
    .delete(apiUrl)
    .then((response) => {
      router.push({
        name: "bicycle-logbook-full",
        params: { id: logBookRecord.value.bicycle.id },
      });
      console.log("Запись успешно удалена:", response.data);
    })
    .catch((error) => {
      errorRecordUpdateMessage.value =
        "Произошла ошибка при удалении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      console.error("Ошибка при удалении записи:", error);
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
            type="file"
            value=""
            accept="image/*"
            @change="handleRecordPicturesUpload"
            multiple
          />
        </div>

        <div v-if="selectedFileNames.length > 0">
          Выбранные файлы:
          <ul>
            <li v-for="(fileName, index) in selectedFileNames" :key="index">
              {{ fileName }}
            </li>
          </ul>
        </div>

        <div
          class="row align-items-center mt-2"
          v-if="logBookRecord.pictures && logBookRecord.pictures.length > 0"
          v-for="picture in logBookRecord.pictures"
          :key="picture.id"
        >
          <div class="col-3">
            <div class="img-wrapper-bike-main-picture">
              <img :src="picture.image" alt="" class="rounded-3 border" />
            </div>
          </div>

          <div class="col">
            <button
              @click.prevent="deletePicture(picture.id)"
              class="btn btn-sm btn-outline-danger rounded-4"
            >
              Удалить фото
            </button>
          </div>
        </div>

        <span class="text-danger" v-if="errorPictureDeleteMessage">
          {{ errorPictureDeleteMessage }}
        </span>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Сохранить изменения
        </button>
      </div>

      <div class="text-center mt-2">
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

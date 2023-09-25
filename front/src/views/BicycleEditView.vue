<script setup>
import { ref, onMounted, computed } from "vue";
import { RouterLink, useRoute } from "vue-router";
import { useStore } from "vuex";
import router from "../router";
import customAxios from "../axios.js";

const bikeId = useRoute().params.id;
const store = useStore();

const userIdFromStore = computed(() => store.state.userId);

const bicycle = ref({});

onMounted(() => {
  let apiUrl = `/my/bicycles/${bikeId}/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      bicycle.value = response.data;
    })
    .catch((error) => {
      console.error("Ошибка при выполнении запроса:", error);
    });
});

const successBicycleUpdateMessage = ref(""); // Сообщение об успешном сохранении
const errorBicycleUpdateMessage = ref(""); // Сообщение об ошибке сохранения
const bicyclePictureUpdateMessage = ref(""); // Информационное сообщение при действиях с фото

// TODO: Можно переписать функционал как в LogBookRecordCreateView (сохранять фото как отдельную модель на бэке)
// Добавляем файл в запрос
const handleBicycleUpdatePictureUpload = (event) => {
  const file = event.target.files[0]; // Берем первый файл (т.к. выбирать на странице можно только один)
  const maxSize = 3 * 1024 * 1024; // 3 МБ в байтах
  if (file && file.size > maxSize) {
    alert("Файл слишком большой. Максимальный размер файла: 3 МБ.");
    event.target.value = ""; // Очистить выбранный файл
    return;
  }
  bicyclePictureUpdateMessage.value = `Изображение "${file.name}" будет загружено после СОХРАНЕНИЯ ИЗМЕНЕНИЙ`;
  bicycle.value.pictures = file;
};

// Создаем временную переменную для отправки данных на сервер
const bicycleForUpdate = computed(() => {
  
  const updatedBicycle = { ...bicycle.value };

  // Если прикреплено новое фото - оставляем updatedBicycle как есть
  if (updatedBicycle.pictures instanceof File) {
  }
  // Если новое фото не прикреплено - удаляем инфо из updatedBicycle, чтоб в запросе оно не отправлялось и действующее фото не изменялось
  else {
    delete updatedBicycle.pictures;
  }
  return updatedBicycle;
});

// TODO: !! Добавить на бэке удаление изображения из папки, при удалении фото в форме
const clearPicture = () => {
  bicycleForUpdate.value.pictures = ""; // Если фото удалено - добавляем в updatedBicycle пустую строку, чтоб затереть существующее фото
  bicyclePictureUpdateMessage.value =
    "Изображение будет удалено при СОХРАНЕНИИ ИЗМЕНЕНИЙ";
};

const updateMyBicycle = () => {
  const apiUrl = `/my/bicycles/${bikeId}/`;

  successBicycleUpdateMessage.value = "";
  errorBicycleUpdateMessage.value = "";
  bicyclePictureUpdateMessage.value = "";

  customAxios
    .put(apiUrl, bicycleForUpdate.value, {
      headers: { "Content-Type": "multipart/form-data" },
    })
    .then((response) => {
      console.log("Информация о велосипеде успешно обновлена:", response.data);
      bicycle.value.pictures = response.data.pictures;
      successBicycleUpdateMessage.value =
        "Информация о велосипеде успешно обновлена.";
    })
    .catch((error) => {
      console.error("Ошибка при редактировании велосипеда:", error);
      errorBicycleUpdateMessage.value =
        "Произошла ошибка при сохранении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку.";
      // TODO: Можно добавить вывод сообщения о причине ошибки пользователю
    });
};

function confirmDelete() {
  if (confirm("Вы уверены, что хотите удалить велосипед?")) {
    deleteMyBicycle();
  }
}

const deleteMyBicycle = () => {
  const apiUrl = `/my/bicycles/${bikeId}/`;

  successBicycleUpdateMessage.value = "";
  errorBicycleUpdateMessage.value = "";

  customAxios
    .delete(apiUrl)
    .then((response) => {
      console.log("Информация о велосипеде успешно удалена:", response.data);
      router.push({
        name: "profile-detail",
        params: { id: userIdFromStore.value },
      });
    })
    .catch((error) => {
      console.error("Ошибка при удалении велосипеда:", error);
      errorBicycleUpdateMessage.value =
        "Произошла ошибка при удалении данных. Пожалуйста, попробуйте ещё раз, или обратитесь в поддержку";
      // TODO: Можно добавить вывод сообщения о причине ошибки пользователю
    });
};
</script>

<template>
  <div class="ms-1 mb-2 fs-3 text-center">Редактировать велосипед</div>
  <div class="card mb-4 rounded-4">
    <form
      class="card-body ms-4 pb-4"
      enctype="multipart/form-data"
      @submit.prevent="updateMyBicycle"
    >
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
          <!-- TODO: не срабатывает selected -->
          <select
            class="form-control"
            id="wheelSize"
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

      <div v-if="bicyclePictureUpdateMessage">
        <div class="row align-items-center mt-2" v-if="bicycle.pictures">
          <div class="col alert alert-primary rounded-4">
            {{ bicyclePictureUpdateMessage }}
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

      <div v-else>
        <div class="row align-items-center mt-2" v-if="bicycle.pictures">
          <div class="col-3">
            <div class="img-wrapper-bike-main-picture">
              <img :src="bicycle.pictures" alt="" class="rounded-3 border" />
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

        <div class="row align-items-center mt-2" v-else>
          <label>
            Фотография
            <span class="text-secondary">
              (максимальный размер файла: 3 МБ.)
            </span>
          </label>
          <div class="col">
            <input
              name="main_pict"
              type="file"
              accept="image/*"
              @change="handleBicycleUpdatePictureUpload"
            />
          </div>
        </div>
      </div>

      <div class="d-flex justify-content-center mt-3">
        <button type="submit" class="btn btn-success w-50 rounded-5">
          Сохранить изменения
        </button>
      </div>
      <div class="text-center mt-2">
        <span
          v-if="successBicycleUpdateMessage"
          class="text-success col-10 ml-2 my-2"
        >
          <p>{{ successBicycleUpdateMessage }}</p>
          <RouterLink
            class="btn border rounded-5"
            :to="{ name: 'bicycle-detail', params: { id: bikeId } }"
          >
            Вернуться к велосипеду
          </RouterLink>
        </span>
        <span v-if="errorBicycleUpdateMessage" class="text-danger col-10 ml-2">
          {{ errorBicycleUpdateMessage }}
        </span>
      </div>
    </form>
  </div>

  <div class="row">
    <div class="col text-en">
      <button
        @click="confirmDelete"
        class="btn btn-sm rounded-5 border btn-outline-danger"
      >
        удалить велосипед
      </button>
    </div>
  </div>
</template>

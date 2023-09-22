<script setup>
import { ref, onMounted, computed } from "vue";
// import axios from "axios";
import customAxios from "../axios.js"
import { useRoute } from "vue-router";
// import BicycleOwnerCardSmall from "../components/logbooks/BicycleOwnerCardSmall.vue";
import { RouterLink } from "vue-router";
import { useStore } from "vuex";

const store = useStore();
const logBookRecordId = useRoute().params.id;

const record = ref([]);
const userIdFromStore = computed(() => store.state.userId);

onMounted(() => {
  let apiUrl = `/logbooks/${logBookRecordId}/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      record.value = response.data;
      // TODO: убрать на проде

      record.value.text = response.data.text
        ? response.data.text.replace(/\n/g, "<br>") //.replace(/ /g, "&nbsp;")
        : "";

      // console.log('response.data------', response.data);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
      console.error("Ошибка при выполнении запроса:", error);
    });
});

// console.log("userIdFromStore----", userIdFromStore);
// console.log('record.creator----', record.value)
</script>

<template>
  <div class="mt-4">
    <div class="">
      <RouterLink
        v-if="record.bicycle"
        class="ms-2 fs-4 text-decoration-none text-dark"
        :to="{ name: 'bicycle-detail', params: { id: record.bicycle.id } }"
      >
        <strong class="">
          {{ record.bicycle.brand }}
          {{ record.bicycle.model }}
          {{ record.bicycle.bicycle_name }}
        </strong>
      </RouterLink>
    </div>

    <div>
      <RouterLink
        v-if="record.bicycle"
        class="ms-2 text-decoration-none text-dark"
        :to="{
          name: 'bicycle-logbook-full',
          params: { id: record.bicycle.id },
        }"
      >
        &lt; в бортжурнал
      </RouterLink>
    </div>
  </div>

  <div class="card shadow-sm mt-3 rounded-4">
    <div class="row g-0">
      <div class="col">
        <div class="card-body">
          <div class="col text-end">
            <div class="row">
              <div class="col">
                <h5 class="card-title mb-0 fs-3 text-start">{{ record.header }}</h5>
              </div>
              <div class="col" v-if="record.creator">
                <RouterLink
                  class="btn btn-sm btn-outline-success rounded-5"
                  v-if="userIdFromStore == record.creator.id"
                  :to="{
                    name: 'logbook-record-edit',
                    params: { id: logBookRecordId },
                  }"
                  >Редактировать</RouterLink
                >
              </div>
            </div>
          </div>

          <p class="card-text">
            <small class="text-muted">{{ record.category }}</small>
          </p>


<div v-if="record && record.pictures && record.pictures.length > 0" v-for="picture in record.pictures">

    <img
      :src="picture.image"
      class="card-img rounded-3 mb-3"
    />
</div>


            <!-- <div class="col img-small">
              <img
                src="https://oboi-telefon.ru/wallpapers/20899/34618.jpg"
                class="card-img-top rounded-3"
                alt="..."
              />
            </div>
            <div class="col img-small">
              <img
                src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg"
                class="card-img-top rounded-3"
                alt="..."
              />
            </div>
            <div class="col img-small">
              <img
                src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg"
                class="card-img-top rounded-3"
                alt="..."
              />
            </div>
             <div class="col img-small">
                <img
                  src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg"
                  class="card-img-top rounded-3"
                  alt="..."
                />
              </div> -->







          <div v-html="record.text" class="card-text mt-4"></div>

          <div class="container mt-3">
            <div class="row">
              <div v-if="record.mileage" class="col-3 text-muted">
                <span>Пробег: {{ record.mileage }} км.</span>
              </div>
              <div class="col-4 text-muted">
                <span v-if="record.cost"
                  >Стоимость: {{ record.cost }} руб.</span
                >
              </div>
              <!-- пустая колонка для корректного отобраения на странице -->
              <div class="col"></div>
              <div class="col text-muted text-end">
                <small>{{ record.created_at }}</small>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
<!-- TODO: !! Добавить кнопки Следующия запись и Предыдущая запись-->


  <!-- TODO: Разобраться со стилями и добавить кнопку "в бортжурнал", 
    т.к. при ее добавлении страница отркывается не сверху, а снизу, 
    как будто уже прокручена до конца-->
  <!-- <div class="container">
    <div class="row row-cols-md-3 mt-2">
      <div class="col d-flex justify-content-center align-items-center">
        <RouterLink class="btn rounded-5 btn-lg border" to="">
          &lt; в бортжурнал
        </RouterLink>
      </div>
      <div class="col">
        <RouterLink class="btn rounded-5 btn-lg w-100 border" to="#">
          Наверх
        </RouterLink>
      </div>
    </div>
  </div> -->
</template>

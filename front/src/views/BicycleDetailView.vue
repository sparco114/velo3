<script setup>
import { ref, onMounted, computed } from "vue";
import { useStore } from "vuex";
import { useRoute, RouterLink } from "vue-router";
import customAxios from "../axios.js";
import BicycleLogBookSmall from "../components/logbooks/BicycleLogBookSmall.vue";
import BicycleOwnerCardSmall from "../components/logbooks/BicycleOwnerCardSmall.vue";
import { DEFAULT_MAIN_BICYCLE_IMAGE } from "../constants.js";

const logBookRecordAmount = "?last=7";
const bikeId = useRoute().params.id;
const store = useStore();

const userIdFromStore = computed(() => store.state.userId);

const bicycle = ref([]);

onMounted(() => {
  let apiUrl = `/bicycles/${bikeId}/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      bicycle.value = response.data;
      // Перезаписываем значение about, заменяя в нем переносы на <br>,
      // а пробелы на &nbsp; чтоб отображать на странице корректное форматирование
      // TODO: можно подумать над другим способом, чтоб не перезаписывать внутри запроса
      // TODO: !! разобраться с безопасностью, т.е. приходится отображать это через v-html= в template
      bicycle.value.about = response.data.about
        ? response.data.about.replace(/\n/g, "<br>") //.replace(/ /g, "&nbsp;")
        : "";
      console.log(response.data);
      console.log(bicycle.value);
    })
    .catch((error) => {
      console.error("Ошибка при выполнении запроса:", error);
    });
});
</script>

<template>
  <!-- TODO: много где проверяется v-if="bicycle, возможно надо вынести его на весь шаблон -->
  <div class="pt-2 pb-2">
    <div class="row">
      <div class="col">
        <h2>
          <strong>
            {{ bicycle.brand }}
            {{ bicycle.model }}
            {{ bicycle.bicycle_name }}
          </strong>
        </h2>
      </div>

      <div class="col">
        <div class="col text-end" v-if="bicycle.owner">
          <RouterLink
            class="btn btn-success rounded-5"
            v-if="userIdFromStore == bicycle.owner.id"
            :to="{ name: 'logbook-record-create', params: { id: bikeId } }"
          >
            Добавить запись
          </RouterLink>
        </div>
      </div>
    </div>
  </div>

  <div class="img-wrapper-bike-main-picture">
    <img
      :src="bicycle.pictures || DEFAULT_MAIN_BICYCLE_IMAGE"
      class="rounded-4 shadow-sm"
      alt="фото велосипеда"
    />
  </div>

  <!-- TODO: если не будет успевать подгружаться, тогда нужен тоже v-if="bicycle.owner" -->
  <BicycleOwnerCardSmall :bicycleOwner="bicycle.owner" />

  <div class="card mt-2 rounded-4">
    <div class="card-body mx-3">
      <div class="row">
        <h5 class="col card-title">О велосипеде</h5>
        <div class="col text-end" v-if="bicycle.owner">
          <RouterLink
            class="btn btn-sm btn-outline-success rounded-5"
            v-if="userIdFromStore == bicycle.owner.id"
            :to="{ name: 'bicycle-edit', params: { id: bicycle.id } }"
          >
            Редактировать
          </RouterLink>
        </div>
      </div>

      <div v-html="bicycle.about" class="card-text"></div>

      <div class="mt-3">
        <strong class="fs-5">ХАРАКТЕРИСТИКИ</strong>
        <ul>
          <li v-if="bicycle.brand">Марка: {{ bicycle.brand }}</li>
          <li v-if="bicycle.model">Модель: {{ bicycle.model }}</li>
          <li v-if="bicycle.release_year">
            Год выпуска: {{ bicycle.release_year }}
          </li>
          <li v-if="bicycle.wheel_size">
            Размер колес: {{ bicycle.wheel_size }}″
          </li>
          <li v-if="bicycle.frame_material">
            Материал рамы: {{ bicycle.frame_material }}
          </li>
          <li v-if="bicycle.purchase_year">
            Был куплен в {{ bicycle.purchase_year }} г.
          </li>
        </ul>
      </div>
    </div>
  </div>

  <div class="mt-4">
    <div class="container g-0">
      <div class="row">
        <div class="col">
          <div class="d-flex">
            <RouterLink
              class="nav-link"
              :to="{ name: 'bicycle-logbook-full', params: { id: bicycle.id } }"
            >
              <h3>Бортжурнал</h3>
            </RouterLink>
          </div>
        </div>

        <div class="col text-end" v-if="bicycle.owner">
          <RouterLink
            class="btn btn-success rounded-5"
            v-if="userIdFromStore == bicycle.owner.id"
            :to="{ name: 'logbook-record-create', params: { id: bikeId } }"
          >
            Добавить запись
          </RouterLink>
        </div>
      </div>
    </div>

    <BicycleLogBookSmall
      :logBookRecordAmount="logBookRecordAmount"
      :bicycleId="bikeId"
    />
  </div>
</template>

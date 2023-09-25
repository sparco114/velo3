<script setup>
import { ref, onMounted, computed } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { useStore } from "vuex";
import customAxios from "../axios.js";

const store = useStore();
const logBookRecordId = useRoute().params.id;

const userIdFromStore = computed(() => store.state.userId);

const record = ref([]);

onMounted(() => {
  let apiUrl = `/logbooks/${logBookRecordId}/`;

  customAxios
    .get(apiUrl)
    .then((response) => {
      record.value = response.data;

      // TODO: Попробовать измежать использование v-html
      record.value.text = response.data.text
        ? response.data.text.replace(/\n/g, "<br>") //.replace(/ /g, "&nbsp;")
        : ""; // Подготовка текста для использования в html формате
    })
    .catch((error) => {
      console.error("Ошибка при выполнении запроса:", error);
    });
});
</script>

<template>
  <div class="mt-4">
    <div>
      <RouterLink
        v-if="record.bicycle"
        class="ms-2 fs-4 text-decoration-none text-dark"
        :to="{ name: 'bicycle-detail', params: { id: record.bicycle.id } }"
      >
        <strong>
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
                <h5 class="card-title mb-0 fs-3 text-start">
                  {{ record.header }}
                </h5>
              </div>

              <div class="col" v-if="record.creator">
                <RouterLink
                  class="btn btn-sm btn-outline-success rounded-5"
                  v-if="userIdFromStore == record.creator.id"
                  :to="{
                    name: 'logbook-record-edit',
                    params: { id: logBookRecordId },
                  }"
                >
                  Редактировать
                </RouterLink>
              </div>
            </div>
          </div>

          <p class="card-text">
            <small class="text-muted">{{ record.category }}</small>
          </p>

          <div
            v-if="record && record.pictures && record.pictures.length > 0"
            v-for="picture in record.pictures"
          >
            <img :src="picture.image" class="card-img rounded-3 mb-3" />
          </div>

          <div v-html="record.text" class="card-text mt-4"></div>

          <div class="container mt-3">
            <div class="row">
              <div v-if="record.mileage" class="col-3 text-muted">
                <span>Пробег: {{ record.mileage }} км.</span>
              </div>

              <div class="col-4 text-muted">
                <span v-if="record.cost">
                  Стоимость: {{ record.cost }} руб.
                </span>
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
</template>

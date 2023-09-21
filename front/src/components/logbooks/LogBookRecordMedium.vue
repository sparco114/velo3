<script setup>
import { defineProps, ref } from "vue";
import { RouterLink } from "vue-router";
import { DEFAULT_MAIN_BICYCLE_IMAGE_URL } from "../../constants.js";

const props = defineProps({
  record: Object,
});

const showFullText = ref({}); // Объект для хранения состояния отображения полного текста
const fullPreparedHtmlText = props.record.text.replace(/\n/g, "<br>");
const shortenedText = props.record.text.slice(0, 255);
const activateShowFull = (recordId) => {
  showFullText.value[recordId] = !showFullText.value[recordId];
};
</script>

<template>
  <div class="card shadow-sm mt-4 rounded-4">
    <div class="row g-0">
      <div class="col-2">
        <!--TODO: доработать, чтоб на разрешении телефона эта часть с инфо о велосипеде уходила вверх, 
        то есть заменить col-2 на col-md-2, но нужно настроить так, чтоб при преходе 
        этой части карточки вверх, название велосипеда отражалось справа от фото велосипеда -->
        <div class="card-body velo-picture">
          <RouterLink
            class="nav-link"
            :to="{ name: 'bicycle-detail', params: { id: record.bicycle.id } }"
          >
            <div class="img-wrapper-bike-main-picture">
              <img
                :src="record.bicycle.pictures || DEFAULT_MAIN_BICYCLE_IMAGE_URL"
                class="card-img"
                alt="фото велосипеда"
              />
            </div>

            <div class="ms-1 mt-1">
              <!-- TODO: можно доработать, чтоб при наведении на пользователя/велосипед 
              появлялось краткое инфо, в том числе город -->
              <div class="">
                {{ record.bicycle.brand }}
                {{ record.bicycle.model }}
                {{ record.bicycle.bicycle_name }}
              </div>
            </div>
          </RouterLink>
          <small class="ms-1 text-muted">{{ record.bicycle.owner }}</small>
        </div>
      </div>
      <div class="col-10">
        <div class="card-body">
          <RouterLink
            class="nav-link"
            :to="{ name: 'logbook-record-detail', params: { id: record.id } }"
          >
            <div v-if="record && record.pictures && record.pictures.length > 0">
              <img :src="record.pictures[0].image" class="card-img rounded-3" />

              <div class="row row-cols-5 g-1 mt-0">
                <template
                  v-for="picture in record.pictures.slice(1, record.pictures.length)"
                >
                  <div class="col">
                    <div class="image-container">
                      <img :src="picture.image" class="rounded-3" />
                    </div>
                  </div>
                </template>
              </div>
            </div>

            <h5 class="card-title mb-0 mt-3">{{ record.header }}</h5>
            <p class="card-text">
              <small class="text-muted">{{ record.category }}</small>
            </p>
          </RouterLink>

          <!-- TODO: попробовать переписать логику, чтоб не было повторения кода -->
          <div class="mt-2">
            <div v-if="record.text.length > 255">
              <div v-if="!showFullText[record.id]">
                {{ shortenedText }}
                <span>
                  <a class="text-nowrap" @click="activateShowFull(record.id)">
                    Читать далее
                  </a>
                </span>
                <p class="card-text text-end">
                  <small class="text-muted">{{ record.created_at }}</small>
                </p>
              </div>
              <div v-else>
                <div v-html="fullPreparedHtmlText"></div>
                <div class="mt-2">
                  <div class="row">
                    <div v-if="record.mileage" class="col-3 text-muted">
                      <small>Пробег: {{ record.mileage }} км.</small>
                    </div>
                    <div class="col-4 text-muted">
                      <small v-if="record.cost"
                        >Стоимость: {{ record.cost }} руб.</small
                      >
                    </div>
                    <div class="col text-muted text-end">
                      <small>{{ record.created_at }}</small>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div v-else>
              {{ record.text }}

              <div class="mt-2">
                <div class="row">
                  <div v-if="record.mileage" class="col-3 text-muted">
                    <small>Пробег: {{ record.mileage }} км.</small>
                  </div>
                  <div class="col-4 text-muted">
                    <small v-if="record.cost"
                      >Стоимость: {{ record.cost }} руб.</small
                    >
                  </div>
                  <div class="col text-muted text-end">
                    <small>{{ record.created_at }}</small>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- TODO: можно добавить кнопку Читать далее, 
            которая будет раскрывать полный текст и добавлять Пробег и Стоимость
            выше нужно будет внести корректировки в функцию showFullText -->
          <!-- <span v-if="record.text.length > 225">
              <RouterLink
                class="text-nowrap"
                to="#"
                 @click="showFullText(record)"
              >
                Читать далее
              </RouterLink> 
            </span> -->
          <!-- </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.image-container {
  position: relative;
  padding-bottom: 62%;
  overflow: hidden;
}

.image-container img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>

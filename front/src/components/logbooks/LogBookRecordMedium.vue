<script setup>
import { defineProps, ref } from "vue";
import { RouterLink } from "vue-router";
import { DEFAULT_MAIN_BICYCLE_IMAGE } from "../../constants.js";

// из LogBookRecordsList и BicycleLogBookFull
const props = defineProps({
  record: Object,
});

const showFullText = ref({}); // Объект для хранения состояния отображения полного текста

const shortText = props.record.text.slice(0, 255); // Начало текста (первые 255 символов)
const fullPreparedHtmlText = props.record.text.replace(/\n/g, "<br>"); // Полный текст

const activateShowFullText = (recordId) => {
  showFullText.value[recordId] = true; // Переключение в режим отображения полного текста
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
                :src="record.bicycle.pictures || DEFAULT_MAIN_BICYCLE_IMAGE"
                class="card-img"
                alt="фото велосипеда"
              />
            </div>

            <!-- TODO: можно доработать, чтоб при наведении на пользователя/велосипед 
              появлялось краткое инфо, в том числе город -->
            <div class="ms-1 mt-1">
              {{ record.bicycle.brand }}
              {{ record.bicycle.model }}
              {{ record.bicycle.bicycle_name }}
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
                <div
                  v-for="picture in record.pictures.slice(
                    1,
                    record.pictures.length
                  )"
                >
                  <div class="col">
                    <div class="image-container">
                      <img :src="picture.image" class="rounded-3" />
                    </div>
                  </div>
                </div>
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
                {{ shortText }}
                <span>
                  <a
                    class="text-nowrap"
                    @click="activateShowFullText(record.id)"
                  >
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
                      <small v-if="record.cost">
                        Стоимость: {{ record.cost }} руб.
                      </small>
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
                    <small v-if="record.cost">
                      Стоимость: {{ record.cost }} руб.
                    </small>
                  </div>

                  <div class="col text-muted text-end">
                    <small>{{ record.created_at }}</small>
                  </div>
                </div>
              </div>
            </div>
          </div>
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

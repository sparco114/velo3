<script setup>
import { defineProps } from "vue";
import { RouterLink } from "vue-router";
import {DEFAULT_MAIN_BICYCLE_IMAGE_URL} from "../../constants.js";


const props = defineProps({
  record: Object,
});

function truncateText(text, maxLength) {
  if (text.length > maxLength) {
    return text.slice(0, maxLength) + "...";
  }
  return text;
}
// TODO: можно добавить кнопку Читать далее,
//             которая будет раскрывать полный текст и добавлять Пробег и Стоимость
//             выше нужно будет ниже есть для эотго заготовка
// function showFullText(record) {
//   // return record.text
//   // TODO: реализовать навигацию на страницу с полным текстом, используя например Vue Router или другой метод навигации
//   console.log("Перейти к полному тексту записи:", record.text);
// }
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
            <div class="">
              <img
                src="https://sun9-20.userapi.com/wr4Sk1RlMsahG6MNaK0SvWAB7X53VZY9Fyf7mg/2LKzqKEWTWE.jpg"
                class="card-img rounded-3"
              />
            </div>

            <div class="row row-cols-md-5 g-1 mt-0">
              <div class="col img-small">
                <img
                  src="https://roliki-magazin.ru/wp-content/uploads/2/6/6/266d0d21749d8e208c20a678723c6535.jpeg"
                  class="card-img-top rounded-3"
                  alt="..."
                />
              </div>
              <div class="col img-small">
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
              </div>
            </div>

            <h5 class="card-title mb-0 mt-3">{{ record.header }}</h5>
            <p class="card-text">
              <small class="text-muted">{{ record.category }}</small>
            </p>
            <div class="card-text">
              {{ truncateText(record.text, 225) }}

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
            </div>
          </RouterLink>
          <p class="card-text text-end">
            <small class="text-muted">{{ record.created_at }}</small>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.img-small img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.img-small {
  height: 5rem;
}
</style>

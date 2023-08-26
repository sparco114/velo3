<script setup>
import { defineProps } from "vue";
import { RouterLink } from "vue-router";

const props = defineProps({
  record: Object,
});

function truncateText(text, maxLength) {
  if (text.length > maxLength) {
    return text.slice(0, maxLength) + "...";
  }
  return text;
}

function showFullText(record) {
  // TODO: реализовать навигацию на страницу с полным текстом, используя например Vue Router или другой метод навигации
  console.log("Перейти к полному тексту записи:", record.text);
}
</script>

<template>
  <div class="card shadow-sm mt-4 rounded-4">
    <div class="row g-0">
      <div class="col-2">
        <!--TODO: доработать, чтоб на разрешении телефона эта часть с инфо о велосипеде уходила вверх, 
        то есть заменить col-2 на col-md-2, но нужно настроить так, чтоб при преходе 
        этой части карточки вверх, название велосипеда отражалось справа от фото велосипеда -->
        <div class="card-body velo-picture">
          <img
            src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg"
            class="card-img"
            alt="..."
          />
          <div class="card-body">
            <p class="">{{ record.bicycle.bicycle_name }}</p>
            <small class="text-muted">{{ record.bicycle.owner }}</small>
          </div>
        </div>
      </div>
      <div class="col-10">
        <div class="card-body">
          <div class="">
            <img
              src="https://sun9-20.userapi.com/wr4Sk1RlMsahG6MNaK0SvWAB7X53VZY9Fyf7mg/2LKzqKEWTWE.jpg"
              class="card-img"
            />
          </div>
          <h5 class="card-title mb-0 mt-3">{{ record.header }}</h5>
          <p class="card-text">
            <small class="text-muted">{{ record.category }}</small>
          </p>
          <div class="card-text">
            {{ truncateText(record.text, 225) }}
            <span v-if="record.text.length > 225">
              <RouterLink
                class="text-nowrap"
                to="#"
                @click.prevent="showFullText(record)"
              >
                Читать далее
              </RouterLink>
            </span>
          </div>
          <p class="card-text text-end">
            <small class="text-muted">{{ record.created_at }}</small>
          </p>
        </div>
      </div>
    </div>
  </div>







</template>

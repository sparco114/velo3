<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import BicycleLogBookSmall from "../components/logbooks/BicycleLogBookSmall.vue";
import BicycleOwnerCardSmall from "../components/logbooks/BicycleOwnerCardSmall.vue";
import { RouterLink } from "vue-router";
import { useStore } from "vuex";

const logBookRecordAmount = "?last=7";
const bikeId = useRoute().params.id;
const store = useStore();

const userIdFromStore = computed(() => store.state.userId);

const bicycle = ref([]);
// console.log('bicycle-----', bicycle.value)

onMounted(() => {
  let apiUrl = `http://127.0.0.1:8000/api/v1/bicycles/${bikeId}/`;

  axios
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
      // TODO: убрать на проде
      console.log(response.data);
      console.log(bicycle.value);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
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
  <div class="img-main">
    <img
      src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg"
      class="rounded-4 shadow-sm"
      alt="..."
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
            >Редактировать</RouterLink
          >
        </div>
      </div>
      <div v-html="bicycle.about" class="card-text"></div>
      <!-- <p class="card-text">{{ bicycle.about }}</p> -->
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

<style>
.img-main {
  height: 30rem;
}

.img-main img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>

<!-- TODO: в будущем доработать, чтоб можно было загружать более одного фото для велосипеда 
  и настроить этот слайдер с фото под ним, чтоб можно было листать. -->
<!-- <template>
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner rounded-4">
    <div class="carousel-item active">
      <div class="img-main">
        <img src="" class="d-block w-100" alt="...">
      </div>
    </div>
    <div class="carousel-item">
      <div class="img-main">
        <img src="" class="d-block w-100" alt="...">
      </div>
    </div>
    <div class="carousel-item">
      <div class="img-main">
        <img src="" class="d-block w-100" alt="...">
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>







<div class="row row-cols- row-cols-md-6 g-2 mt-1 justify-content-center  border">
  <div class="col img-small border">
      <img src="https://roliki-magazin.ru/wp-content/uploads/2/6/6/266d0d21749d8e208c20a678723c6535.jpeg" class="card-img-top rounded-3" alt="...">
  </div>
  <div class="col img-small  ">
      <img src="https://oboi-telefon.ru/wallpapers/20899/34618.jpg" class="card-img-top rounded-3" alt="...">
  </div>
  <div class="col img-small  border">
      <img src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg" class="card-img-top rounded-3" alt="...">
  </div>
  <div class="col img-small border">
      <img src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg" class="card-img-top rounded-3" alt="...">
  </div>
  <div class="col img-small">
      <img src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg" class="card-img-top rounded-3" alt="...">
  </div>
  <div class="col img-small border">
      <img src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg" class="card-img-top rounded-3" alt="...">
  </div>
  
  
</div>



</template>


<style>
.img-main {
  height: 30rem; 
}

.img-main img {
  width: 100%; 
  height: 100%;
  object-fit: cover; 
}

.img-small img {
  width: 100%; 
  height: 100%; 
  object-fit: cover; 
}

.img-small {
  height: 5rem;
}

</style> -->

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useRoute } from "vue-router";
import BicycleLogBookSmall from "../components/logbooks/BicycleLogBookSmall.vue";
import BicycleOwnerCardSmall from "../components/logbooks/BicycleOwnerCardSmall.vue";
import { RouterLink } from "vue-router";

const logBookRecordAmount = "?last=7";
const bikeId = useRoute().params.id;

const bicycle = ref([]);

onMounted(() => {
  let apiUrl = `http://127.0.0.1:8000/api/v1/bicycles/${bikeId}/`;

  axios
    .get(apiUrl)
    .then((response) => {
      bicycle.value = response.data;
      // TODO: убрать на проде
      console.log(response.data);
    })
    .catch((error) => {
      // TODO: изменить на запись в лог и вывод текста пользователю
      console.error("Ошибка при выполнении запроса:", error);
    });
});

</script>

<template>
  <div class="pt-2">
    <h2>
      <strong>
        {{ bicycle.brand }}
        {{ bicycle.model }}
        {{ bicycle.bicycle_name }}
      </strong>
    </h2>
  </div>
  <div class="img-main">
    <img
      src="http://www.mtbtestcentral.it/wp-content/uploads/2019/06/Orbea-Laufey-4-1536x1024.jpg"
      class="rounded-4 shadow-sm"
      alt="..."
    />
  </div>

  






<BicycleOwnerCardSmall :bicycleOwner="bicycle.owner" />






  <div class="card mt-2 rounded-4">
    <div class="card-body">
      <h5 class="card-title">О велосипеде</h5>
      <!-- <h6 class="card-subtitle mb-2 text-body-secondary">Card subtitle</h6> -->
      <p class="card-text">{{ bicycle.about }}</p>
      <div class="mt-">
        <strong>ХАРАКТЕРИСТИКИ</strong>
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
    <BicycleLogBookSmall :logBookRecordAmount="logBookRecordAmount" :bicycleId="bikeId"/>
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

.avatar {
  width: 3rem;
  height: 3rem;
}

.avatar img {
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

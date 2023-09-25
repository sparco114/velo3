<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import ProfileDetail from "../components/profiles/ProfileDetail.vue";
</script>

<!-- Вынесено в отдельный компонент, т.к. требуется чтоб компонент рендерился каждый раз, 
когда меняется id в адресной строке. Проблема возникала, если находясь на  странице другого 
пользователя нажать "Мой профиль", будет изменен id в адресной строке, и нежен ререндеринг станицы. -->
<template>
  <router-view :key="computed(() => useRoute().params.id)">
    <ProfileDetail />
  </router-view>
</template>

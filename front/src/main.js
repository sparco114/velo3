import "./assets/main.css";

// import axios from "axios";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

const app = createApp(App);

const authToken = localStorage.getItem("authToken");
const userId = localStorage.getItem("userId");

// TODO: проверить все ли случаи обрабатываются
if (authToken && userId) {
  // console.log('сработал иф, записывается токен')
  store.commit("setAuthTokenFromLocalStorage", authToken);
  store.commit("setUserIdFromLocalStorage", userId);
  console.log("setAuthTokenFromLocalStorage--", authToken);
  console.log("setUserIdFromLocalStorage--", userId);
} else {
  store.commit("clearAuthToken");
  store.commit("clearUserId");
  console.log("Нет токена или userId в LocalStorage");
}

app.use(store);
app.use(router);

app.mount("#app");

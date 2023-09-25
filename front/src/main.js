import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./assets/main.css";

const app = createApp(App);

const authToken = localStorage.getItem("authToken");
const userId = localStorage.getItem("userId");

// TODO: проверить все ли случаи обрабатываются
if (authToken && userId) {
  store.commit("setAuthTokenFromLocalStorage", authToken); // записываем токен в vue store, если он есть в LocalStorage
  store.commit("setUserIdFromLocalStorage", userId); // записываем id в vue store, если он есть в LocalStorage
  // console.log("setAuthTokenFromLocalStorage--", authToken);
  // console.log("setUserIdFromLocalStorage--", userId);
} else {
  store.commit("clearAuthToken");
  store.commit("clearUserId");
  console.log("Нет токена или userId в LocalStorage");
}

// перенесено в axios.js
// axios.defaults.baseURL = "http://127.0.0.1:8000/api/v1";

app.use(store);
app.use(router);

app.mount("#app");

// TODO: !! на проде убрать все console.log из всех компонентов. Вместо этого можно записывать в лог

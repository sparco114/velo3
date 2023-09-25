import { createStore } from "vuex";
import customAxios from "./axios";

/* Создается хранилище Vuex, в которое записывается токен авторизации и
id пользователя, если он есть в localStorage (действие выполянется в main.js)
Если информации нет в localStorage, тогда юзер логинится на сайте, и после этого
токен и id сохраняются в localStorage и в store.
Запись этой информации инициируется функцией loginUser в UserLogInView.vue.
Удаление этой информации инициируется функцией logout в NavBar.vue
А так же для всех axios запросов добавляется/удаляется заголовок Authorization,
в котором указан токен */
const store = createStore({
  state: {
    authToken: null,
    userId: null,
    /* TODO: можно добавить сюда состояния (успешно, загрузка, ошибка),
    чтобы в зависимости от него отображать соответствующий контент или выполнять действия,
    например колесико загрузки или переход на страницу после успешного входа */
  },

  mutations: {
    // Сохраняем токен в state (если он уже есть в localStorage, т.е. пользователь залогинен ранее)
    setAuthTokenFromLocalStorage(state, token) {
      state.authToken = token;
      customAxios.defaults.headers.common["Authorization"] = `Token ${token}`;
    },

    // Сохраняем токен в state и в localStorage (получаяя из API, т.е. пользователю нужно залогинитсья)
    setAuthTokenFromApi(state, token) {
      localStorage.setItem("authToken", token);
      state.authToken = token;
      customAxios.defaults.headers.common["Authorization"] = `Token ${token}`;
    },

    // Удаляем токен из state и из localStorage (при логауте пользователя)
    clearAuthToken(state) {
      localStorage.removeItem("authToken");
      state.authToken = null;
      customAxios.defaults.headers.common["Authorization"] = null;
    },

    // Сохраняем id в state (если он уже есть в localStorage, т.е. пользователь залогинен ранее)
    setUserIdFromLocalStorage(state, userId) {
      state.userId = userId;
    },

    // Сохраняем id в state и в localStorage (получаяя из API, т.е. пользователю нужно залогинитсья)
    setUserIdFromFromApi(state, userId) {
      localStorage.setItem("userId", userId);
      state.userId = userId;
    },

    // Удаляем токен из state и из localStorage (при логауте пользователя)
    clearUserId(state) {
      localStorage.removeItem("userId");
      state.userId = null;
    },
  },
});

export default store;

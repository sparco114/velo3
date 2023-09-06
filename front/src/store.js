import { createStore } from "vuex";
// import axios from "axios";
import customAxios from "./axios"


// Отправляется запрос на сервер для получения id залогиненого юзера
// (требуется при входе юзера или при перезагрузке старницы)
// async function fetchUserId(token) {
//   try {
//     console.log('получен токен в фетч', token);
//     const userResponse = await axios.get(
//       "http://127.0.0.1:8000/api/v1/djoser_auth/users/me/",
//       {
//         headers: {
//           Authorization: `Token ${token}`,
//         },
//       }
//     );
//     console.log('userResponse вернул ', userResponse.data);

//     const userId = userResponse.data.id;
//     // store.commit('setUserId', userId);
//     console.log("userId--fetched succ", userId);
//     return userId;
//   } catch (error) {
//     console.error('Error fetching user data:', error);
//     return null;
//   }
// }







// Создается хранилище Vuex, в которое записывается токен авторизации, в момент,
// когда он добавляется в localStorage.
// В localStorage он записывается функцией loginUser в UserLogInView.vue.
// Удаляется из localStorage функцией logout в NavBar.vue
// А так же для всех axios запросов добавляется/удаляется заголовок Authorization,
// в котором указан токен
const store = createStore({
  state: {
    // authToken: localStorage.getItem('authToken')
    authToken: null,
    userId: null,
    // TODO: можно добавить сюда состояния (успешно, загрузка, ошибка),
    // чтобы в зависимости от него отображать соответствующий контент или выполнять действия,
    // например колесико загрузки или переход на страницу после успешного входа
  },
  mutations: {
    setAuthTokenFromLocalStorage(state, token) {
      state.authToken = token;
      customAxios.defaults.headers.common["Authorization"] = `Token ${token}`;
      // console.log("сейчас вызовется фетч");
      // state.userId = fetchUserId(token);
      // state.userId = await fetchUserId(token);
      // fetchUserId(token).then(userId => {
      //   state.userId = userId; // Присваиваем userId после разрешения промиса
      //   });
      // console.log('fetchUserId при Локал Сторе вернул -------', state.userId)
    },
    setAuthTokenFromApi(state, token) {
      localStorage.setItem("authToken", token);
      state.authToken = token;
      customAxios.defaults.headers.common["Authorization"] = `Token ${token}`;
      // state.userId = fetchUserId(token);
      // fetchUserId(token).then(userId => {
      //   state.userId = userId; // Присваиваем userId после разрешения промиса
      //   });
      // console.log('fetchUserId при Апи вернул -------', state.userId)
    },
    clearAuthToken(state) {
      localStorage.removeItem("authToken");
      state.authToken = null;
      customAxios.defaults.headers.common["Authorization"] = null;
    },
    setUserIdFromLocalStorage(state, userId) {
      state.userId = userId; // Сохраняем идентификатор пользователя
    },
    setUserIdFromFromApi(state, userId) {
      localStorage.setItem("userId", userId);
      state.userId = userId; // Сохраняем идентификатор пользователя
    },
    clearUserId(state) {
      localStorage.removeItem("userId");
      state.userId = null; // Сохраняем идентификатор пользователя
    },
  },
});

export default store;

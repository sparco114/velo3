import { createStore } from 'vuex';

// Создается хранилище Vuex, в которое записывается токен авторизации, в момент, 
// когда он добавляется в localStorage. 
// В localStorage он записывается функцией loginUser в UserLogInView.vue. 
// Удаляется из localStorage функцией logout в NavBar.vue
// TODO: Перенести кнопку Выход в актуальное место сайта, и откорректировать описание выше.
const store = createStore({
  state: {
    authToken: localStorage.getItem('authToken')
    // TODO: можно добавить сюда состояния (успешно, загрузка, ошибка), 
    // чтобы в зависимости от него отображать соответствующий контент или выполнять действия,
    // например колесико загрузки или переход на страницу после успешного входа
  },
  mutations: {
    setAuthToken(state, token) {
        localStorage.setItem('authToken', token);
        state.authToken = token;
    },
    clearAuthToken(state) {
        localStorage.removeItem('authToken');
        state.authToken = null;
    }
  }
});

export default store;

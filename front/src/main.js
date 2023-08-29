import './assets/main.css'

import axios from 'axios';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

const authToken = localStorage.getItem('authToken');
if (authToken) {
    // Добавляется токен авторизации пользователя в заголовки каждого запроса
    //  (если он существует в хранилище)
    axios.defaults.headers.common['Authorization'] = `Token ${authToken}`;
}

// Добавляет глобальную переменную $authTokenExist, которая отражает наличие токена
app.config.globalProperties.$authTokenExist = authToken ? true : false

app.use(router)

app.mount('#app')

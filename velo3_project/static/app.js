//TODO: если будет много компонентов, можно разледить их по файлам, как указано в разделе Splitting Up the Modules документации  https://vuejs.org/guide/quick-start.html#creating-a-vue-application

//TODO: на проде надо использовать версию вью https://unpkg.com/vue@3/dist/vue.esm-browser.prod.js
import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

export const bicyclesListApp = createApp({
  data() {
    return {
      bicycles: []
    };
  },
  mounted() {
    let apiUrl = 'http://127.0.0.1:8000/api/v1/bicycles/';
    if (window.location.pathname === '/bicycles/') {
      apiUrl += '?ordering=-id';
//      TODO: добавить пагинацию для страницы /bicycles/
    } else {
      apiUrl += '?random=3';
    }
  axios.get(apiUrl)
    .then(response => {
        this.bicycles = response.data.results;
        console.log(response.data)
    })
    .catch(error => {
        console.error('Ошибка при выполнении запроса:', error);
    });
  },
//  template: `
//    <div>
//      <h1>List of Bicycles</h1>
//      <ul>
//        <li v-for="bike in bicycles">
//          <strong>{{ bike.bicycle_name }}</strong> - {{ bike.owner }}<br>
//          Brand: {{ bike.brand }}, Model: {{ bike.model }}<br>
//        </li>
//      </ul>
//    </div>
//  `,
});






export const logbookRecordsListApp = createApp({
  data() {
    return {
      logbook_records: []
    };
  },
  methods: {
        truncateText(text, maxLength) {
            if (text.length > maxLength) {
                return text.slice(0, maxLength) + '...';
            }
            return text;
        },
        showFullText(record) {
            // TODO: реализовать навигацию на страницу с полным текстом, используя например Vue Router или другой метод навигации
            console.log('Перейти к полному тексту записи:', record.text);
        }
  },
  mounted() {
      axios.get('http://127.0.0.1:8000/api/v1/logbooks/?random=7')
        .then(response => {
            this.logbook_records = response.data.results;
            console.log(response.data)

      })
        .catch(error => {
            console.error('Ошибка при выполнении запроса:', error);
      });
  },
});


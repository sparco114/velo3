//TODO: если будет много компонентов, можно разледить их по файлам, как указано в разделе Splitting Up the Modules документации  https://vuejs.org/guide/quick-start.html#creating-a-vue-application

const { createApp } = Vue

const bicycles_app = createApp({
  data() {
    return {
      bicycles: []
    };
  },
  mounted() {
      axios.get('http://127.0.0.1:8000/api/v1/bicycles/?random=3')
        .then(response => {
            this.bicycles = response.data;
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

bicycles_app.mount('#bicycles_list_app');





const logbook_records_app = createApp({
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
            this.logbook_records = response.data;
      })
        .catch(error => {
            console.error('Ошибка при выполнении запроса:', error);
      });
  },
});

logbook_records_app.mount('#logbook_records_list_app');
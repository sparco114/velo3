//TODO: если будет много компонентов, можно разледить их по файлам, как указано в разделе Splitting Up the Modules документации  https://vuejs.org/guide/quick-start.html#creating-a-vue-application

const { createApp } = Vue

const bicycles_app = createApp({
  data() {
    return {
      bicycles: []
    };
  },
  mounted() {
      axios.get('http://127.0.0.1:8000/api/v1/bicycles/')
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
  mounted() {
      axios.get('http://127.0.0.1:8000/api/v1/logbooks/')
        .then(response => {
            this.logbook_records = response.data;
      })
        .catch(error => {
            console.error('Ошибка при выполнении запроса:', error);
      });
  },
});

logbook_records_app.mount('#logbook_records_list_app');
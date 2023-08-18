const bicycles_app = Vue.createApp({
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
});

//компоненты можно переиспользовать, когда будет необходимость, чтоб не дублировать код
//bicycles_app.component('bicycle-list', {
//  props: ['bicycles'],
////  template: `
////    <div>
////      <h1>List of Bicycles</h1>
////      <ul>
////        <li v-for="bike in bicycles" :key="bike.id">
////          <strong>{{ bike.bicycle_name }}</strong> - {{ bike.owner }}<br>
////          Brand: {{ bike.brand }}, Model: {{ bike.model }}<br>
////          Price: {{ bike.price }}
////        </li>
////      </ul>
////    </div>
////  `
//});

bicycles_app.mount('#bicycles_list_app');
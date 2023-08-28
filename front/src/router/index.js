import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BicyclesView from '../views/BicyclesView.vue'
import LogBookRecordsView from '../views/LogBookRecordsView.vue'
import BicycleDetailView from '../views/BicycleDetailView.vue'
import LogBookRecordDetailView from '../views/LogBookRecordDetailView.vue'
import BicycleLogBookFullView from '../views/BicycleLogBookFullView.vue'
import ProfileDetailView from '../views/ProfileDetailView.vue'
import UserRegistrationView from '../views/UserRegistrationView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },    
    {
      path: '/bicycles',
      name: 'bicycles-list',
      component: BicyclesView
    },
    {
      path: '/logbooks',
      name: 'logbooks-list',
      component: LogBookRecordsView
    },
    {
      path: '/bicycles/:id',
      name: 'bicycle-detail',
      component: BicycleDetailView
    },
    {
      path: '/logbooks/:id',
      name: 'logbook-record-detail',
      component: LogBookRecordDetailView
    },
    {
      path: '/bicycles/:id/logbook',
      name: 'bicycle-logbook-full',
      component: BicycleLogBookFullView
    },
    {
      path: '/profiles/:id',
      name: 'profile-detail',
      component: ProfileDetailView
    },
    {
      path: '/registration',
      name: 'user-registration',
      component: UserRegistrationView
    },


    // {
    //   path: '/bicycles',
    //   name: 'bicycles',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/BicyclesView.vue')
    // }
  ],
  scrollBehavior() {
    return { top: 0 }; // Прокрутка страницы в начало при каждом переходе
  },
})

export default router

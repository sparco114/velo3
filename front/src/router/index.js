import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import BicyclesView from '../views/BicyclesView.vue'
import LogBookRecordsView from '../views/LogBookRecordsView.vue'
import BicycleDetailView from '../views/BicycleDetailView.vue'
import LogBookRecordDetailView from '../views/LogBookRecordDetailView.vue'
import BicycleLogBookFullView from '../views/BicycleLogBookFullView.vue'
import ProfileDetailView from '../views/ProfileDetailView.vue'
import UserRegistrationView from '../views/UserRegistrationView.vue'
import UserLogInView from '../views/UserLogInView.vue'
import ProfileEditView from '../views/ProfileEditView.vue'
import BicycleCreateView from '../views/BicycleCreateView.vue'
import BicycleEditView from '../views/BicycleEditView.vue'
import LogBookRecordCreateView from '../views/LogBookRecordCreateView.vue'
import LogBookRecordEditView from '../views/LogBookRecordEditView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import AboutProjectView from '../views/AboutProjectView.vue'
import AgreementView from '../views/AgreementView.vue'
import ConfidentialPolicyView from '../views/ConfidentialPolicyView.vue'
import SupportView from '../views/SupportView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },    
    {
      path: '/bicycles',
      name: 'bicycles-list',
      component: BicyclesView,
    },
    {
      path: '/logbooks',
      name: 'logbooks-list',
      component: LogBookRecordsView,
    },
    {
      path: '/bicycles/:id',
      name: 'bicycle-detail',
      component: BicycleDetailView,
    },
    {
      path: '/logbooks/:id',
      name: 'logbook-record-detail',
      component: LogBookRecordDetailView,
    },
    {
      path: '/bicycles/:id/logbook',
      name: 'bicycle-logbook-full',
      component: BicycleLogBookFullView,
    },
    {
      path: '/profiles/:id',
      name: 'profile-detail',
      component: ProfileDetailView,
    },
    {
      path: '/registration',
      name: 'user-registration',
      component: UserRegistrationView,
    },
    {
      path: '/login',
      name: 'user-login',
      component: UserLogInView,
    },
    {
      path: '/profiles/my/edit',
      name: 'profile-edit',
      component: ProfileEditView,
    },
    {
      path: '/my/bicycles/create',
      name: 'bicycle-create',
      component: BicycleCreateView,
    },
    {
      path: '/my/bicycles/:id',
      name: 'bicycle-edit',
      component: BicycleEditView,
    },
    {
      path: '/bicycles/:id/logbook/create',
      name: 'logbook-record-create',
      component: LogBookRecordCreateView,
    },
    {
      path: '/logbook/:id/edit',
      name: 'logbook-record-edit',
      component: LogBookRecordEditView,
    },
    {
      path: '/404',
      name: 'not-found-page',
      component: NotFoundView,
    },
    // TODO: При попадении на стнаицу NotFoundView невозможно вернуться на предыдущую станицу стрелкой Назад
    { path: '/:pathMatch(.*)*',
      name: 'not-found-path', 
      component: NotFoundView ,
    },
    {
      path: '/about-project',
      name: 'about-project',
      component: AboutProjectView,
    },
    {
      path: '/agreement',
      name: 'agreement',
      component: AgreementView,
    },
    {
      path: '/confidential-policy',
      name: 'confidential-policy',
      component: ConfidentialPolicyView,
    },
    {
      path: '/support',
      name: 'support',
      component: SupportView,
    },
    
    // Динамический импорт
    // {
    //   path: '/bicycles',
    //   name: 'bicycles',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/BicyclesView.vue')
    // }
  ],

// TODO: страницы не всегда открываются с начала(сверху). Попробовать решить это другим способом.
  scrollBehavior() {
    return { top: 0 }; // Прокрутка страницы в начало при каждом переходе
  },
})

export default router;

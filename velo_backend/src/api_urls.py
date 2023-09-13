from django.conf.urls import url
from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter, DefaultRouter

from src.bicycles.views import BicycleListViewSet, MyBicycleListViewSet, MyBicycleCreateViewSet, MyBicycleUpdateViewSet, \
    BicycleDetailViewSet
from src.logbooks.views import LogBookRecordViewSet, BicycleLogBookViewSet, BicycleLogBookRecordCreateView, \
    LogBookRecordUpdateView
from src.profiles.views import MyVeloUserView, VeloUserViewSet


urlpatterns = [
    # path('profiles/', include('src.profiles.urls')),
    # path('', include('src.logbooks.urls')),

    path('drf_auth/', include('rest_framework.urls')),  # стандартный вход drf (по сессиям)
    path('djoser_auth/', include('djoser.urls')),  # регистрация djoser и остальные эндпойнты
    path('djoser_token/', include('djoser.urls.authtoken')),  # вход djoser (по токену)


    # TODO: Проверить возможность переписать это на роутеры
    path('profiles/', VeloUserViewSet.as_view({'get': 'list'})),  # просмотр
    path('profiles/<int:pk>/', VeloUserViewSet.as_view({'get': 'retrieve'})),  # просмотр
    path('my/profile/', MyVeloUserView.as_view(), name='my-profile'),  # (редактирование, удаление)


    path('bicycles/', BicycleListViewSet.as_view({'get': 'list'})),  # просмотр
    path('bicycles/<int:pk>/', BicycleDetailViewSet.as_view({'get': 'retrieve'})),  # просмотр
    path('my/bicycles/', MyBicycleListViewSet.as_view({'get': 'list'})),  # просмотр, возможно не пригодится, если не будет отдельной стрницы для моих велосипедов
    path('my/bicycles/create/', MyBicycleCreateViewSet.as_view()),  # (создание)
    path('my/bicycles/<int:pk>/', MyBicycleUpdateViewSet.as_view()),  # (редактирование, удаление)


    path('bicycles/<int:pk>/logbook/', BicycleLogBookViewSet.as_view({'get': 'list'})),  # просмотр
    path('bicycles/<int:pk>/logbook/create/', BicycleLogBookRecordCreateView.as_view()),  # (создание)
    #
    path('logbooks/<int:pk>/', LogBookRecordViewSet.as_view({'get': 'retrieve'})),  # просмотр
    path('logbooks/<int:pk>/update/', LogBookRecordUpdateView.as_view()),  # (редактирование)
    path('logbooks/', LogBookRecordViewSet.as_view({'get': 'list'})),  # просмотр
]

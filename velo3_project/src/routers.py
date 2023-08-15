from django.urls import include, path

from src.bicycles.views import BicycleViewSet
from src.profiles.views import MyVeloUserView, VeloUserViewSet

urlpatterns = [
    # path('profiles/', include('src.profiles.urls')),
    # path('bicycles/', include('src.bicycles.urls')),
    # path('', include('src.logbooks.urls')),
    # TODO: либо распределить эти пути по файлам urls.py в каждом приложении, либо удалить эти файлы, если они не будут использованы
    path('profiles/', VeloUserViewSet.as_view({'get': 'list'})),  # просмотр
    path('profiles/<int:pk>/', VeloUserViewSet.as_view({'get': 'retrieve'})),  # просмотр
    path('my/profile/', MyVeloUserView.as_view(), name='my-profile'),  # (редактирование, удаление)


    path('bicycles/', BicycleViewSet.as_view({'get': 'list'})),  # просмотр
    path('bicycles/<int:pk>/', BicycleViewSet.as_view({'get': 'retrieve'})),  # просмотр
    # path('my/bicycles/', ),  # просмотр
    # path('my/bicycle/add/', BicycleViewSet.as_view({'post': 'create'})),  # (создание)
    # path('my/bicycles/<int:pk>/', BicycleViewSet.as_view({'get': 'retrieve',
    #                                                       'patch': 'partial_update',
    #                                                       'put': 'update',
    #                                                       'delete': 'destroy'})),  # (редактирование, удаление)
    # path('bicycles/<int:pk>/logbook/', ),  # просмотр
    # path('bicycles/<int:pk>/logbook/add/', ),  # (создание)
    #
    # path('logbooks/<int:pk>/', ),  # просмотр
    # path('logbooks/<int:pk>/edit/', ),  # (редактирование)
    # path('logbooks/', ),  # просмотр
]

"""
api/v1/profiles/ -- просмотр
api/v1/profiles/1 -- просмотр
api/v1/profiles/my/ -- (редактирование, удаление)


api/v1/bicycles/ -- просмотр
api/v1/bicycles/1 -- просмотр
api/v1/my/bicycles/ -- просмотр
api/v1/my/bicycles/add -- (создание)
api/v1/my/bicycles/1 -- (редактирование, удаление)



api/v1/bicycles/1/logbook/ -- просмотр
api/v1/bicycles/1/logbook/add -- (создание)

api/v1/logbooks/1 -- просмотр
api/v1/logbooks/1/edit -- (редактирование)
api/v1/logbooks/ -- просмотр

"""

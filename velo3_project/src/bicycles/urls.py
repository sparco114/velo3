# from rest_framework.routers import SimpleRouter
# from src.bicycles.views import BicycleViewSet
#
# router = SimpleRouter()
#
# router.register(r'', BicycleViewSet)
#
# urlpatterns = router.urls
#
from django.urls import path

from src.bicycles.views import bicycles_list

urlpatterns = [
    path('bicycles/', bicycles_list),
]

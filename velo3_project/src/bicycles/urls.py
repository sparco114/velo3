from rest_framework.routers import SimpleRouter, DefaultRouter
from src.bicycles.models import Bicycle

router = SimpleRouter()

router.register(r'', Bicycle)

urlpatterns = router.urls


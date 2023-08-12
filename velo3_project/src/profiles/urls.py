from rest_framework.routers import SimpleRouter

from src.profiles.views import VeloUserViewSet, VeloUserProfileViewSet

router = SimpleRouter()

router.register('velouser', VeloUserViewSet)
router.register('velouserprofile', VeloUserProfileViewSet)

urlpatterns = router.urls

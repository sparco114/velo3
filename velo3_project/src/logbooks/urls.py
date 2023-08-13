from rest_framework.routers import SimpleRouter

from src.logbooks.views import LogBookRecordViewSet

router = SimpleRouter()

# TODO: откорректировать адреса во всех моделях, чтоб были по типу .../пользователь/велосипед/запись
router.register('', LogBookRecordViewSet)

urlpatterns = router.urls

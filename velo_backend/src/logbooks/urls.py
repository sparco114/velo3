# from django.urls import path, include
# from rest_framework.routers import SimpleRouter
#
# from src.logbooks.views import LogBookRecordViewSet
#
# logbook_records_router = SimpleRouter()
#
# logbook_records_router.register('add', LogBookRecordViewSet)
#
#
# urlpatterns = [
#     path('bicycles/<int:bicycle_pk>/', include(logbook_records_router.urls)),
#     path('logbook_records_list/', LogBookRecordViewSet.as_view({'get': 'list'})),
# ]
#
#

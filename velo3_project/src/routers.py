from django.urls import include, path


urlpatterns = [
    path('profiles/', include('src.profiles.urls')),
    path('bicycles/', include('src.bicycles.urls')),
    path('logbooks/', include('src.logbooks.urls')),
]


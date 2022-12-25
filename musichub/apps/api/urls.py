from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()

urlpatterns = (
    path('', include('apps.users.urls')),
    path('audio/', include('apps.audio_library.urls'))
)

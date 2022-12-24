from django.contrib import admin
from django.template.defaulttags import url
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.api.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Foodgram API",
        default_version='v1',
        description="Документация для приложения Foodgram"
    ), public=True, permission_classes=[permissions.AllowAny, ],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    path(
        'redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]

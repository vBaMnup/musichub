from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.users.endpoint import views


app_name = 'users'

router = DefaultRouter()


urlpatterns = [
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('author/', views.AuthorView.as_view({'get': 'list'})),
    path('author/<int:pk>/', views.AuthorView.as_view({'get': 'retrieve'})),
    path('social/', views.SocialLinkView.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('social/<int:pk>/', views.SocialLinkView.as_view(
        {'put': 'update',
         'delete': 'destroy'}
    )),
    path('', include(router.urls)),
    path('', include("djoser.urls")),
    path('auth/', include('djoser.urls.authtoken')),
]
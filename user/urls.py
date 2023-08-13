from rest_framework import routers
from django.urls import path, include
from knox import views as knox_views
from .api import UserAPI

router = routers.DefaultRouter()

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/user', UserAPI.as_view()),
    path('auth/login/', KnoxLoginView.as_view(), name='knox_login'),
    path('auth/register/', register_user, name='register_user'),
]

urlpatterns += router.urls

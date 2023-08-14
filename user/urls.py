from rest_framework import routers
from django.urls import path, include
from knox import views as knox_views
from .api import UserAPI, RegisterAPI, LoginAPI

router = routers.DefaultRouter()

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view())
]

urlpatterns += router.urls

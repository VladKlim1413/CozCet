from knox.models import AuthToken
from rest_framework import permissions, generics
from .models import UserModel
from .serializers import UserSerializer
from knox.views import LoginView as KnoxLoginView
from django.urls import path
# from .views import UserAPI, register_user


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

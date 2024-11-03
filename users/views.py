from rest_framework import generics

from users.serializers import UserRegisterSerializer


# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер для регистрации пользователя"""
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

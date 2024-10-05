
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.authentication import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from cats_apiapp.models import Kittens
from .serializers import Users_serializer, Cats_Serializer


class RegistrationUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Users_serializer.RegistrationUserSerializer

    def post(self, request):
        serializer = Users_serializer.RegistrationUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('mamuka1')
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            print('mamuka', refresh)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })


class LoginAPIView(APIView):
    serializer_class = Users_serializer.LoginSerializer

    def post(self, request) -> Response:
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(request, username=username,password=password)
        if user is None:
            return Response({'Ошибка':'Неверный пароль или имя пользователя'},
                            status=status.HTTP_401_UNAUTHORIZED)
        return Response({"Успешно":"Вход выполнен!"},
                        status=status.HTTP_201_CREATED)


class KittensViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Kittens.objects.all()
    serializer_class = Cats_Serializer.KittensSerializer


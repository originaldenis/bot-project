from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class RegistrationUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя.
    """
    email = serializers.EmailField(allow_null=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']

    def validate_email(self, value:str) -> str:
        """
        Метод для проверки электронной почты
        :param value: str
        :return: str
        """
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с такой почтой уже зарегистрирован')
        return email

    def validation_password(self, value):
        validate_password(value)
        return value


class LoginSerializer(serializers.ModelSerializer):
    """
    Сериализатор для логина пользователей.
    """
    class Meta:
        model = User
        fields = ['username', 'password']

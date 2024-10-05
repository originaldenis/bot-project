from rest_framework import serializers
from cats_apiapp.models import Kittens


class KittensSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели кошек
    """
    class Meta:
        model = Kittens
        fields = '__all__'
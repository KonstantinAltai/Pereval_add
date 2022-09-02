from rest_framework import serializers
from .models import Pereval, Level, Author
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', )


class AuthorSerializer(serializers.ModelSerializer):
    user =UserSerializer(read_only=True)
    class Meta:
        model = Author
        exclude = ('id',)

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        # fields='__all__'
        exclude = ('id',)

class PerevalSerializer(serializers.ModelSerializer):
    levels = LevelSerializer(read_only=True)
    user = AuthorSerializer(read_only=True)
    #levels = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Pereval
        # fields= '__all__'
        exclude = ('id', 'status')

class PerevalDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Pereval
        exclude = ('id', )

class PerevalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval

from rest_framework import serializers
from .models import Pereval, Author, User, Images



class AuthorSerializer(serializers.ModelSerializer):
    '''Данные автора'''
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'otc', 'email', 'phone', ]


class PerevalSerializer(serializers.ModelSerializer):
    '''Список перевалов'''
    user = AuthorSerializer(read_only=True)
    levels = serializers.StringRelatedField(many=True)
    #img = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Images-detail')
    class Meta:
        model = Pereval
        fields = ['user', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'lofitude', 'logitude', 'height', 'levels'
                ]


class PerevalDetailSerializer(serializers.ModelSerializer):
    '''Сведения по перевалу'''
    #user = AuthorSerializer(read_only=True)
    class Meta:
        model = Pereval
        fields = '__all__'

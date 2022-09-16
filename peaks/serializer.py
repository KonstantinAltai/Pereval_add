from rest_framework import serializers
from .models import Pereval, Author, Level, Images


class AuthorSerializer(serializers.ModelSerializer):
    '''Данные автора'''
    class Meta:
        model = Author
        fields = ('email', 'first_name', 'last_name', 'otc', 'phone')


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ('season', 'level')


class ImagesSerializer(serializers.ModelSerializer):
    pereval = serializers.CharField(source='pereval.title')

    class Meta:
        model = Images
        fields = ('data', 'title', 'pereval')


class PerevalSerializer(serializers.ModelSerializer):
    '''Список перевалов'''
    user = AuthorSerializer(read_only=True)
    levels = serializers.StringRelatedField(required=False, many=True)
    img = ImagesSerializer(required=False, many=True)

    class Meta:
        model = Pereval
        fields = ('id', 'user', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'lofitude', 'logitude', 'height', 'levels', 'img'
                  )

    def create(self, validated_data):
        return Pereval.objects.create(**validated_data)

    """def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance"""


class PerevalDetailSerializer(serializers.ModelSerializer):
    '''Сведения по перевалу'''
    user = AuthorSerializer(read_only=True)
    levels = serializers.StringRelatedField(required=False, many=True)
    #levels = serializers.StringRelatedField(many=True)
    img = ImagesSerializer(required=False, many=True)

    class Meta:
        model = Pereval
        fields = ('status', 'beauty_title', 'title', 'other_titles', 'connect',
                  'add_time', 'user', 'lofitude', 'logitude', 'height', 'levels', 'img'
                  )


class PerevalCreateSerializer(serializers.ModelSerializer):
    '''Добаавление сведений о перавале'''
    class Meta:
        model = Pereval
        fields = '__all__'
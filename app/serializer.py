from rest_framework import serializers
from app.models import Game


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    uuid = serializers.UUIDField(read_only  = True)
    is_active = serializers.BooleanField(read_only=True)
    name = serializers.CharField()
    url = serializers.URLField()
    author = serializers.CharField()
    publised_date = serializers.DateField()

    def create(self, validated_data):
        return Game.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.url = validated_data.get('url', instance.url)
        instance.author = validated_data.get('author', instance.author)
        instance.publised_date = validated_data.get('publised_date', instance.publised_date)
        instance.save()
        return instance
    
    
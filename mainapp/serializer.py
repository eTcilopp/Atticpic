from rest_framework import serializers

from mainapp.models import Artworks


class CreateArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artworks
        exclude = ('id_author',)


class ReadArtworkSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='id_author')
    category = serializers.CharField(source='id_category')

    class Meta:
        model = Artworks
        fields = (
            'id',
            'artwork',
            'name',
            'description',
            'status',
            'date_create',
            'date_update',
            'author',
            'category',
        )


class ListArtworkSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='id_author')
    category = serializers.CharField(source='id_category')

    class Meta:
        model = Artworks
        fields = (
            'id',
            'artwork',
            'name',
            'description',
            'status',
            'date_create',
            'date_update',
            'author',
            'category',
        )

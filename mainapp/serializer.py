from rest_framework import serializers

from mainapp.models import Artworks


class CreateArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artworks
        exclude = ('id_author',)


class ReadArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artworks
        fields = '__all__'


class ListArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artworks
        fields = '__all__'

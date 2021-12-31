from rest_framework import serializers
from authapp.models import UserProfile


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'avatar')


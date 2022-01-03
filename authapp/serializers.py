from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from authapp.models import UserProfile
from django.db import IntegrityError


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'avatar')


class CustomUserCreateSerializer(UserCreateSerializer):

    def create_unique_username(self):
        counter = 0
        while True:
            counter += 1
            new_username = f'User{counter}'
            try:
                UserProfile.objects.get(username=new_username)
            except UserProfile.DoesNotExist:
                return new_username

    def create(self, validated_data):
        validated_data['username'] = self.create_unique_username()
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

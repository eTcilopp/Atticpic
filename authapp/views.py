from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from authapp.models import UserProfile
from authapp.serializers import UserAvatarSerializer


class UserAvatarUploadView(generics.CreateAPIView):
    '''
    POST - загрузка аватара пользователя. /auth/avatar/{"avatar": [image file]}
    '''
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        profile = UserProfile.objects.get(id=request.user.id)
        serializer = UserAvatarSerializer(
            profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request):
        profile = UserProfile.objects.get(id=request.user.id)
        profile.avatar = 'users_avatars/default.png'
        profile.save()
        return JsonResponse({'response': 'Аватар удален'}, status=200)

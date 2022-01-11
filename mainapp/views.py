import datetime

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import BasePermission

from mainapp.serializer import *


class IsObjectOwner(BasePermission):
    message = "Редактирование не разрешено."
    my_safe_methods = ['PUT', 'PATCH', 'DELETE']

    def has_permission(self, request, view):
        if request.method in self.my_safe_methods:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return obj
        else:
            return obj == request.user


class CreateArtworkView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CreateArtworkSerializer

    def perform_create(self, serializer):
        return serializer.save(id_author=self.request.user)


class RetrieveArtworkView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ReadArtworkSerializer
    queryset = Artworks.objects.exclude(status='Del').all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        try:
            obj = queryset.get(id=self.kwargs['id'])
        except Artworks.DoesNotExist:
            obj = None
        finally:
            return obj


class UpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsObjectOwner, permissions.IsAuthenticated, ]
    serializer_class = ReadArtworkSerializer
    queryset = Artworks.objects.exclude(status='Del').all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        try:
            obj = queryset.get(id=self.kwargs['id'])
        except Artworks.DoesNotExist:
            obj = None
        finally:
            return obj

    def perform_destroy(self, instance):
        instance.status = 'Del'
        instance.save()

class ListArtworkView(generics.ListAPIView):
    serializer_class = ListArtworkSerializer
    def get_queryset(self):
        return Artworks.objects.exclude(status='Del').all()


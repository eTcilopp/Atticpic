from django.urls import path, include, reverse_lazy
from authapp.views import UserAvatarUploadView

app_name = 'authapp'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('avatar/', UserAvatarUploadView.as_view())
]

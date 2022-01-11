from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('artwork/create/', CreateArtworkView.as_view()),
    path('artwork/read/<int:id>/', RetrieveArtworkView.as_view()),
    path('artwork/update/<int:id>/', UpdateDestroyView.as_view()),
    path('artwork/list/all/', ListArtworkView.as_view()),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

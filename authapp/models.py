import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserProfile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), blank=False, unique=True)
    avatar = models.ImageField(upload_to='users_avatars', default='users_avatars/default.png', blank=True,
                               verbose_name='Аватар')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

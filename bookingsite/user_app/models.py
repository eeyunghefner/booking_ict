from django.contrib.auth.models import AbstractUser
from django.db import models

from .enums import UserType
from .manager import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField("Адрес электронной почты",
                              unique=True)
    type = models.CharField("Тип пользователя",
                            max_length=64,
                            choices=UserType.choices,
                            default=UserType.BUYER)

    profile_image = models.ImageField("Изображение профиля",
                                      blank=True,
                                      null=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
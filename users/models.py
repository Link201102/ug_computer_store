from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    phone = models.CharField("Телефон", max_length=11, null=True, blank=True)
    address = models.CharField("Адрес", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

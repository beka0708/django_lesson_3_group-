from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=100)
    citi = models.CharField(max_length=100)
    image = models.ImageField(upload_to="", blank=True)

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователь"

    def __str__(self):
        return self.username

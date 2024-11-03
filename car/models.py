from django.db import models


class Car(models.Model):
    CAR_TYPE = {
        ("Седан", "Седан"),
        ("Купе", "Купе"),
        ("Универсал", "Универсал"),
        ("Кабриолет", "Кабриолет")
    }
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    car_type = models.CharField(max_length=50, choices=CAR_TYPE)
    video = models.URLField()

    def __str__(self):
        return self.title

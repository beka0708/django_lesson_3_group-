from django.db import models


class Car(models.Model):
    CAR_TYPE = {
        ("Седан", "Седан"),
        ("Купе", "Купе"),
        ("Универсал", "Универсал"),
        ("Кабриолет", "Кабриолет")
    }
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Фото", upload_to="")
    created_date = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField("Цена", help_text="Цену нужно писать в долларах")
    car_type = models.CharField("Тип машины", max_length=50, choices=CAR_TYPE)
    video = models.URLField("Ссылка")

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return self.title


class CommentCar(models.Model):
    RATE = {
        ("*", "*"),
        ("**", "**"),
        ("***", "***"),
        ("****", "****"),
        ("*****", "*****"),
    }
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car")
    text = models.TextField()
    rate = models.CharField(max_length=17, choices=RATE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car.title

# Generated by Django 5.1.2 on 2024-11-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_alter_car_car_type_alter_commentcar_car_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Седан', 'Седан'), ('Кабриолет', 'Кабриолет'), ('Купе', 'Купе'), ('Универсал', 'Универсал')], max_length=50, verbose_name='Тип машины'),
        ),
        migrations.AlterField(
            model_name='commentcar',
            name='rate',
            field=models.CharField(choices=[(4, 4), (5, 5), (3, 3), (2, 2), (1, 1)], max_length=17),
        ),
    ]

from django.db import models
from django.urls import reverse


# Create your models here.
class Region(models.Model):
    name = models.CharField("Название региона", blank=True, max_length=50)
    square = models.IntegerField("Площадь территорий", blank=True)


class City(models.Model):
    name = models.CharField("Название города", blank=True, max_length=30)
    age = models.IntegerField("Возраст", blank=True)
    reg = models.ForeignKey(Region, models.DO_NOTHING)
    def get_absolute_url(self):
        return f'/'

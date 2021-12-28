from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField("Название города", max_length=30)
    age = models.IntegerField("Возраст")
    flag = models.ImageField("Герб")

class Region(models.Model):
    name = models.CharField("Название региона", max_length=50)
    square = models.IntegerField("Площадь территорий")
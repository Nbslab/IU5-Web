from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField("Название региона", max_length=50)
    square = models.IntegerField("Площадь территорий")


class City(models.Model):
    name = models.CharField("Название города", max_length=30)
    age = models.IntegerField("Возраст")
    flag = models.ImageField("Герб")
    reg = models.ForeignKey(Region, models.DO_NOTHING)
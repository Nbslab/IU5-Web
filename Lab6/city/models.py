from django.db import models


class PCs(models.Model):
    name = models.CharField('Название', max_length=30)
    op_system = models.CharField('Операционная система', max_length=50)
    ram_storage = models.DecimalField('Объем операционной памяти', decimal_places=3, max_digits=10)

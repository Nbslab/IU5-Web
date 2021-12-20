from django.db import models


class PCs(models.Model):
    name = models.CharField('Название', max_length=30)
    op_system = models.CharField('Операционная система', max_length=50)


class Programs(models.Model):
    name = models.CharField('Название', max_length=30)
    storage_usage = models.DecimalField('Занимаемый объем памяти', decimal_places=3, max_digits=10)
    pcs = models.ForeignKey(PCs, models.DO_NOTHING)

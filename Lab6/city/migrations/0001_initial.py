# Generated by Django 4.0 on 2021-12-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PCs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('op_system', models.CharField(max_length=50, verbose_name='Операционная система')),
                ('ram_storage', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Объем операционной памяти')),
            ],
        ),
    ]

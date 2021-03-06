# Generated by Django 4.0 on 2021-12-28 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название региона')),
                ('square', models.IntegerField(verbose_name='Площадь территорий')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название города')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('flag', models.ImageField(upload_to='', verbose_name='Герб')),
                ('reg', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='city.region')),
            ],
        ),
    ]

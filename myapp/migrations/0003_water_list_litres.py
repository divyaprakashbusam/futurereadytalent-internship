# Generated by Django 2.1.15 on 2022-01-13 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_water_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='water_list',
            name='litres',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

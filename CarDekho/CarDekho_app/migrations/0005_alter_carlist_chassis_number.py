# Generated by Django 5.1.4 on 2024-12-26 12:42

import CarDekho_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0004_alter_carlist_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlist',
            name='chassis_number',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[CarDekho_app.models.alphanumeric]),
        ),
    ]

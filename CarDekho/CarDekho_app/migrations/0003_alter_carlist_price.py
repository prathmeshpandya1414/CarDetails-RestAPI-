# Generated by Django 5.1.4 on 2024-12-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0002_carlist_chassis_number_carlist_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]

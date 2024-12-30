# Generated by Django 5.1.4 on 2024-12-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='chassis_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carlist',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

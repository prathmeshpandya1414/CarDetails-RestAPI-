# Generated by Django 5.1.4 on 2024-12-28 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho_app', '0006_showroomlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='showroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showrooms', to='CarDekho_app.showroomlist'),
        ),
    ]

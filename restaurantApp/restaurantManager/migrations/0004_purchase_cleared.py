# Generated by Django 4.2.11 on 2024-05-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0003_recipereq_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='cleared',
            field=models.BooleanField(default=False),
        ),
    ]

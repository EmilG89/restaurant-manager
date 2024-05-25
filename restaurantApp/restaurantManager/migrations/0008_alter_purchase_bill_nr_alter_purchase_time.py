# Generated by Django 4.2.11 on 2024-05-12 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0007_alter_purchase_bill_nr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='bill_nr',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

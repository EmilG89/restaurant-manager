# Generated by Django 4.2.11 on 2024-05-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0006_alter_purchase_menu_item_alter_recipereq_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='bill_nr',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]

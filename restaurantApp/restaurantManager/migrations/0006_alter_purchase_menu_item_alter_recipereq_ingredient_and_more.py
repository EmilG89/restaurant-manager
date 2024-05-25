# Generated by Django 4.2.11 on 2024-05-09 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0005_purchase_bill_nr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='menu_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='restaurantManager.menuitem'),
        ),
        migrations.AlterField(
            model_name='recipereq',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantManager.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipereq',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantManager.menuitem'),
        ),
    ]

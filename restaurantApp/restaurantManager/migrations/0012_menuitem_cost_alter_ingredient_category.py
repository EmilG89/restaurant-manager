# Generated by Django 4.2.11 on 2024-06-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0011_ingredient_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.CharField(choices=[('FRESH PRODUCE', 'FRESH PRODUCE'), ('GRAINS', 'GRAINS'), ('MEAT / PROTEIN', 'MEAT / PROTEIN'), ('DAIRY', 'DAIRY'), ('BAKING GOODS', 'BAKING GOODS'), ('FREEZER', 'FREEZER'), ('CANNED / DRIED GOODS', 'CANNED / DRIED GOODS'), ('CONDIMENTS / SPICES', 'CONDIMENTS / SPICES'), ('OILS / VINEGARS', 'OILS / VINEGARS'), ('SNACKS', 'SNACKS'), ('OTHER', 'OTHER')], default='OTHER', max_length=20),
        ),
    ]

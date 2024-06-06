# Generated by Django 4.2.11 on 2024-06-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0010_alter_ingredient_options_alter_purchase_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.CharField(choices=[('FRESH PRODUCE', ''), ('GRAINS', ''), ('MEAT / PROTEIN', ''), ('DAIRY', ''), ('BAKING GOODS', ''), ('FREEZER', ''), ('CANNED / DRIED GOODS', ''), ('CONDIMENTS / SPICES', ''), ('OILS / VINEGARS', ''), ('SNACKS', ''), ('OTHER', '')], default='OTHER', max_length=20),
        ),
    ]
import csv
from .models import Ingredient
import random

# Run this script to populate Ingredient table with provided csv table,
# where table consists of 4 clumns - Ingredient 1.Name, 2.Category, 
# 3.Unit, 4.Price. 
# In csv file Column 5 Quantity can be included if quntity is 
# provided. In this case script needs to be updated to pass column
# data to Ingredient Model.

# to run script, use command line:
# echo 'import restaurantManager.populate' | python3 manage.py shell

with open("restaurantManager/static/restaurantManager/ingredients.csv", newline='') as ingredient_table:
    ingredients = csv.DictReader(ingredient_table, delimiter=';')
    for ingredient in ingredients:
        item = Ingredient(name=ingredient['Name'], 
                        category=ingredient['Category'],
                        unit=ingredient['Unit'],
                        quantity=random.randint(5, 25), 
                        price=ingredient['Price'])
        item.save()
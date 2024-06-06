from django.db import models
from datetime import datetime, timezone
from django.utils import timezone

# Create your models here.
class Ingredient(models.Model):
    UNIT_TYPES = [
        ("l", "litre"),
        ("kg", "kilogramm"),
        ("bottle", "bottle"),
        ("eggs", "eggs")
    ]

    CATEGORIES = [
        ('FRESH PRODUCE', 'FRESH PRODUCE'),
        ('GRAINS', 'GRAINS'),
        ('MEAT / PROTEIN', 'MEAT / PROTEIN'),
        ('DAIRY', 'DAIRY'),
        ('BAKING GOODS', 'BAKING GOODS'),
        ('FREEZER', 'FREEZER'),
        ('CANNED / DRIED GOODS', 'CANNED / DRIED GOODS'),
        ('CONDIMENTS / SPICES', 'CONDIMENTS / SPICES'),
        ('OILS / VINEGARS', 'OILS / VINEGARS'),
        ('SNACKS', 'SNACKS'),
        ('OTHER', 'OTHER')
    ]

    name = models.CharField(unique = True, max_length=30)
    unit = models.CharField(max_length=10, choices=UNIT_TYPES)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='OTHER')

    class Meta:
        ordering = ['name']

    def stock_value(self):
        return self.price * self.quantity

    def get_absolute_url(self):
        return "/ingredients"
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(unique = True, max_length=30)
    price = models.FloatField(default=0)
    cost = models.FloatField(default=0)

    class Meta:
        ordering = ['name']

    def calculate(self):
        recipe_req = RecipeReq.objects.filter(menu_item__name = self.name)
        item_cost = 0
        for ingredient in recipe_req:
            item_cost += ingredient.converter() * ingredient.ingredient.price
        return item_cost

    def get_absolute_url(self):
        return "/menu_items"
    
    def __str__(self):
        return self.name

class RecipeReq(models.Model):
    UNIT_TYPES = [
        ("tbs", "table spoon"),
        ("ml", "mililitres"),
        ("g", "grams"),
        ("eggs", "eggs"),
        ("bottle", "bottle")
    ]

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    unit = models.CharField(max_length=10, default="-", choices=UNIT_TYPES)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return "/recipe_req/%i/create" % self.menu_item.pk
    
    def converter(self):
        if self.unit == "tbs":
            return 0.05 * self.amount
        elif self.unit == "ml":
            return 0.001 * self.amount
        elif self.unit == "g":
            return 0.001 * self.amount
        elif self.unit == "eggs":
            return 1 * self.amount
        elif self.unit == "bottle":
            return 1 * self.amount

class Purchase(models.Model):

    time = models.DateTimeField(default = timezone.now)
    menu_item = models.ForeignKey(MenuItem, default= None, on_delete=models.PROTECT)
    cleared = models.BooleanField(default=False)
    bill_nr = models.IntegerField(default=0)

    class Meta:
        ordering = ['-time']

#    def __init__(self):
#        self.bill_nr = 
    
#    def __str__(self):
#        return str(self.bill_nr)

    def get_absolute_url(self):
        return "/purchases"
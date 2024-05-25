from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeReq, Purchase

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeReq)
admin.site.register(Purchase)
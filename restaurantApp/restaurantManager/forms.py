from django import forms, forms
from .models import Ingredient, MenuItem, RecipeReq, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ("name", "price")

class RecipeReqForm(forms.ModelForm):
    class Meta:
        model = RecipeReq
        fields = ("ingredient", "unit", "amount", "menu_item")

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

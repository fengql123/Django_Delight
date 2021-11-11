from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase


class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "quantity", "unit", "unit_price"]


class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "quantity", "unit", "unit_price"]


class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "price"]


class MenuUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "price"]


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["menu_item", "timestamp"]


class PurchaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ["menu_item", "timestamp"]

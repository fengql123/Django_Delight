from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientCreateForm, IngredientUpdateForm, MenuCreateForm, MenuUpdateForm, PurchaseCreateForm, PurchaseUpdateForm


def home(request):
    context = {"name": "fql"}
    return render(request, "inventory/home.html", context)


class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"


class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "inventory/ingredientcreate.html"
    form_class = IngredientCreateForm


class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredientupdate.html"
    form_class = IngredientUpdateForm


class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredientdelete.html"
    success_url = "/ingredients/"


class MenuList(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


class MenuCreate(CreateView):
    model = MenuItem
    template_name = "inventory/menucreate.html"
    form_class = MenuCreateForm


class MenuUpdate(UpdateView):
    model = MenuItem
    template_name = "inventory/menuupdate.html"
    form_class = MenuUpdateForm


class MenuDelete(DeleteView):
    model = MenuItem
    template_name = "inventory/menudelete.html"
    success_url = "/menu/"


class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase.html"


class PurchaseCreate(CreateView):
    model = Purchase
    template_name = "inventory/purchasecreate.html"
    form_class = PurchaseCreateForm


class PurchaseUpdate(UpdateView):
    model = Purchase
    template_name = "inventory/purchaseupdate.html"
    form_class = PurchaseUpdateForm


class PurchaseDelete(DeleteView):
    model = Purchase
    template_name = "inventory/purchasedelete.html"
    success_url = "/purchase/"

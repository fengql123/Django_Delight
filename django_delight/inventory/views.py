from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientCreateForm, IngredientUpdateForm, MenuCreateForm, MenuUpdateForm, PurchaseCreateForm, PurchaseUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy


def logout_view(request):
    # ... Other logic
    logout(request)
    return redirect("home")


@login_required
def home(request):
    context = {"name": request.user}
    return render(request, "inventory/home.html", context)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"


class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/ingredientcreate.html"
    form_class = IngredientCreateForm


class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/ingredientupdate.html"
    form_class = IngredientUpdateForm


class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredientdelete.html"
    success_url = "/ingredients/"


class MenuList(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


class MenuCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menucreate.html"
    form_class = MenuCreateForm


class MenuUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "inventory/menuupdate.html"
    form_class = MenuUpdateForm


class MenuDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/menudelete.html"
    success_url = "/menu/"


class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase.html"


class PurchaseCreate(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/purchasecreate.html"
    form_class = PurchaseCreateForm


class PurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/purchaseupdate.html"
    form_class = PurchaseUpdateForm


class PurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/purchasedelete.html"
    success_url = "/purchase/"

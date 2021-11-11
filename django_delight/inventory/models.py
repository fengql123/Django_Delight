from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=5)
    unit_price = models.IntegerField()

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return self.name


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=5)

    def get_absolute_url(self):
        return "/menu"


class Purchase(models.Model):
    menu_item = menu_item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def get_absolute_url(self):
        return "/purchase"

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls"), name="login"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path('ingredients/', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredients/create', views.IngredientCreate.as_view(),
         name='ingredientcreate'),
    path('ingredients/update/<pk>', views.IngredientUpdate.as_view(),
         name='ingredientupdate'),
    path('ingredients/delete/<pk>', views.IngredientDelete.as_view(),
         name='ingredientdelete'),
    path('menu/', views.MenuList.as_view(), name='menulist'),
    path('menu/create', views.MenuCreate.as_view(),
         name='menucreate'),
    path('menu/update/<pk>', views.MenuUpdate.as_view(),
         name='menuupdate'),
    path('menu/delete/<pk>', views.MenuDelete.as_view(),
         name='menudelete'),
    path('purchase/', views.PurchaseList.as_view(), name='purchaselist'),
    path('purchase/create', views.PurchaseCreate.as_view(),
         name='purchasecreate'),
    path('purchase/update/<pk>', views.PurchaseUpdate.as_view(),
         name='purchaseupdate'),
    path('purchase/delete/<pk>', views.PurchaseDelete.as_view(),
         name='purchasedelete'),
]

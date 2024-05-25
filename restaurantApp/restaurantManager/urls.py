from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/<args>/', views.home, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('ingredients/create/', views.CreateIngredientView.as_view(), name='create_ingredient'),
    path('ingredients/<pk>/update/', views.UpdateIngredientView.as_view(), name='update_ingredient'),
    path('ingredients/<pk>/delete/', views.DeleteIngredientView.as_view(), name='delete_ingredient'),
    path('menu_items/', views.MenuItemsView.as_view(), name='menu_items'),
    path('menu_items/create/', views.CreateMenuItemView.as_view(), name='create_menu_item'),
    path('menu_items/<pk>/update/', views.UpdateMenuItemView.as_view(), name='update_menu_item'),
    path('menu_item/<pk>/delete/', views.DeleteMenuItemView.as_view(), name='delete_menu_item'),
    path('recipe_req/<pk>/', views.RecipeReqView.as_view(), name='recipe_req'),
    path('recipe_req/<pk>/create/', views.CreateRecipeReqView.as_view(), name='create_recipe_req'),
    path('recipe_req/<pk>/<pk2>/update/', views.UpdateRecipeReqView.as_view(), name='update_recipe_req'),
    path('recipe_req/<pk>/<pk2>/delete/', views.DeleteRecipeReqView.as_view(), name='delete_recipe_req'),
    path('purchases/', views.PurchasesView.as_view(), name='purchases'),
    path('purchases/create/<pk>/', views.CreatePurchaseView.as_view(), name='create_purchase'),
    path('purchase/<pk>/update/', views.UpdatePurchaseView.as_view(), name='update_purchase'),
    path('purchase/<pk>/delete/', views.DeletePurchaseView.as_view(), name='delete_purchase')
]
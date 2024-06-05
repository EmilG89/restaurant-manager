from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ingredient, MenuItem, RecipeReq, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeReqForm, PurchaseForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from datetime import datetime, timedelta

MENU_ITEMS = MenuItem.objects.all()
INGREDIENTS = Ingredient.objects.all()

# Create your views here.
def login_view(request):
    context = {
        "login_view": "active"
    }

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Wrong username or password!")
            return render(request, "registration/login.html", context)
    
    return render(request, "registration/login.html", context)

#Could use UserCreationForm
def register_view(request):
    context = {
        "register_view": "pending"
    }

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        r_password = request.POST["r_password"]

        if len(username) >= 4 and password == r_password:
            try:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                return redirect('login')
            except:
                messages.info(request, "username or email already exist")
                return render(request, "registration/register.html")
        else:
            messages.info(request, "Username must be at least 4 characters long or passwords dont match.")
            return render(request, "registration/register.html", context)
    
    return render(request, "registration/register.html", context)
    
def logout_view(request):
    logout(request)
    return redirect('login')

#Could use TemplateView
@login_required
def home(request, **kwargs):

    context = {
        "name": "Dashboard",
        "table_header": "Last 10 purchases",
        "purchase_count": [],
        "money": {},
        "daily_data": [],
        "money_total": [0, 0, 0]
    }

    context['last_purchases'] = Purchase.objects.all().order_by('-id')[:10]
    context['item_name'] = MenuItem.objects.values_list('name')

    for item in MenuItem.objects.values('name'):
        context['purchase_count'].append((item['name'], Purchase.objects.filter(menu_item__name = item['name']).count()))

    purchases_today = Purchase.objects.filter(time__gte = datetime.today().astimezone().strftime("%Y-%m-%d 00:00:00.000000 %z"))
    total_income = 0
    total_cost = 0
    for purchase in purchases_today:
        total_income += purchase.menu_item.price
        for cost in RecipeReq.objects.filter(menu_item = purchase.menu_item):
            total_cost += cost.converter() * cost.ingredient.price

    context["money"].update({'income': "%.2f €"%(total_income,), 'cost': f"{total_cost:.2f} €", 'profit': "{:.2f} €".format(total_income - total_cost)})

    for day in range(15):
        x = datetime.now().astimezone() - timedelta(days=day)
        y = x + timedelta(days=1)
        purchases = Purchase.objects.filter(time__range = (x.strftime("%Y-%m-%d 00:00:00.000000 %z"), y.strftime("%Y-%m-%d 00:00:00.000000 %z")))
        daily_income = 0
        daily_cost = 0

        for purchase in purchases:
            daily_income += purchase.menu_item.price
            item_cost = 0
            for cost in RecipeReq.objects.filter(menu_item = purchase.menu_item):
                item_cost += cost.converter() * cost.ingredient.price
            daily_cost += item_cost

        context['daily_data'].append([round(daily_income, 2), round(daily_cost, 2), round((daily_income - daily_cost), 2), x.strftime("%Y-%m-%d")])
        context['money_total'] = [round(x + y, 2) for x, y in zip(context['money_total'], [daily_income, daily_cost, daily_income - daily_cost])]

    if request.method == "POST" and kwargs.get('args') == 'time':
        #add try
        start_date = request.POST['start_date']
        start_time = request.POST['start_time']
        end_date = request.POST['end_date']
        end_time = request.POST['end_time']
        
        start = " ".join([start_date, start_time+":00.000000+03:00"])
        end = " ".join([end_date, end_time+":00.000000+03:00"])
        purchases = Purchase.objects.filter(time__gte = start).exclude(time__gte = end)
        context['last_purchases'] = purchases
        context['table_header'] = " ".join([start_date, start_time]) + " - " + " ".join([end_date, end_time])

        return render(request, "restaurantManager/home.html", context)

    if request.method == "POST" and kwargs.get('args') == 'item':
        items = Purchase.objects.filter(menu_item = MenuItem.objects.get(name = request.POST['item'])).order_by('-id')
        context['items'] = items

        return render(request, "restaurantManager/home.html", context)
    
    return render(request, "restaurantManager/home.html", context)

class IngredientsView(LoginRequiredMixin, ListView):
    model = Ingredient

    def get_context_data(self):
        context = super().get_context_data()
        ingredients_values = [ingredient.quantity * ingredient.price for ingredient in INGREDIENTS]
        context['ingredients'] = INGREDIENTS
        #use @register to create custom function that can find
        #item by key inside template
        context['total_value'] = sum(ingredients_values)
        return context

    template_name = "restaurantManager/ingredients.html"

class CreateIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "restaurantManager/create_ingredient.html"

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    def get_context_data(self):
        context = super().get_context_data()
        context['ingredients'] = INGREDIENTS
        return context
    template_name = "restaurantManager/update_ingredient.html"

class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['ingredients'] = INGREDIENTS
        return context
    template_name = "restaurantManager/delete_ingredient.html"
    success_url = reverse_lazy('ingredients')

class MenuItemsView(LoginRequiredMixin, ListView):
    model = MenuItem

    def get_context_data(self):
        context = super().get_context_data()
        context['recipes'] = RecipeReq.objects.values_list('menu_item', flat=True)
        context['menu_items'] = MENU_ITEMS           
        return context

    template_name = "restaurantManager/menu_items.html"

class CreateMenuItemView(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    def get_context_data(self):
        context = super().get_context_data()
        context['menu_items'] = MENU_ITEMS
        return context
    template_name = "restaurantManager/create_menu_item.html"

class UpdateMenuItemView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    def get_context_data(self):
        context = super().get_context_data()
        context['menu_items'] = MENU_ITEMS
        return context
    template_name = "restaurantManager/update_menu_item.html"

class DeleteMenuItemView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu_items'] = MENU_ITEMS
        return context
    template_name = "restaurantManager/delete_menu_item.html"
    success_url = reverse_lazy('menu_items')

class RecipeReqView(LoginRequiredMixin, ListView):
    model = RecipeReq
    template_name = "restaurantManager/recipe_req.html"

class CreateRecipeReqView(LoginRequiredMixin, CreateView):
    model = RecipeReq
    form_class = RecipeReqForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = RecipeReq.objects.filter(menu_item = self.kwargs.get('pk'))
        context['form'] = RecipeReqForm(initial={'menu_item': self.kwargs.get('pk')})
        return context
    
    template_name = "restaurantManager/create_recipe_req.html"

class UpdateRecipeReqView(LoginRequiredMixin, UpdateView):
    model = RecipeReq
    form_class = RecipeReqForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = RecipeReq.objects.filter(menu_item = self.kwargs.get('pk2'))
        return context
    
    template_name = "restaurantManager/update_recipe_req.html"

class DeleteRecipeReqView(LoginRequiredMixin, DeleteView):
    model = RecipeReq

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = RecipeReq.objects.filter(menu_item = self.kwargs.get('pk2'))
        return context

    def get_success_url(self):
        item = RecipeReq.objects.get(pk = self.kwargs.get('pk'))
        return reverse_lazy('create_recipe_req', kwargs={'pk': item.menu_item.pk})
    
    template_name = "restaurantManager/delete_recipe_req.html"
    
class PurchasesView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "restaurantManager/purchases.html"

class CreatePurchaseView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm

    def get(self, request, **kwargs):
        item = MenuItem.objects.get(pk = kwargs.get('pk'))
        req = RecipeReq.objects.filter(menu_item = item.pk)
        for ing in req:
            i = Ingredient.objects.filter(name=ing.ingredient.name).first()
            if ing.converter() > i.quantity:
                messages.info(request, "out of {}".format(i.name))
                return redirect('menu_items')
            else:
                i.quantity = round(i.quantity - ing.converter(), 3)
                i.save()
        b = Purchase(menu_item = item)
        b.save()
        return redirect(reverse_lazy('menu_items'))
    
    template_name = "restaurantManager/create_purchase.html"

class UpdatePurchaseView(LoginRequiredMixin, UpdateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "restaurantManager/update_purchase.html"

class DeletePurchaseView(LoginRequiredMixin, DeleteView):
    model = Purchase
    form_class = PurchaseForm
    template_name = "restaurantManager/delete_purchase.html"

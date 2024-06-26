from django.shortcuts import render,redirect
from .models import *
from django.core.cache import cache
# Create your views here.


def all_products(request):
    # Dynamically generate cache keys based on model names
    product_cache_key = 'Product_all'
    categories_cache_key = 'Categories_all'

    # Try to get products and categories from cache
    item = cache.get(product_cache_key)
    categories = cache.get(categories_cache_key)
    # print("coming from cache")

    # If products or categories are not in cache, fetch from database and set cache
    if item is None:
        item = list(Product.objects.all())  # Convert queryset to list for caching
        cache.set(product_cache_key, item, timeout=300)  # Cache for 5 minutes
        # print('coming from db')
        
    
    if categories is None:
        categories = list(Categories.objects.all())  # Convert queryset to list for caching
        cache.set(categories_cache_key, categories, timeout=300)  # Cache for 5 minutes

    # Render the template with the context
    return render(request, 'index.html', context={"item": item, "categories": categories})


def get_categories_response(request,uuid):
    category = Categories.objects.get(uuid=uuid)
    item = Product.objects.filter(categories = category)
    # print(item)
    return render(request,'product_categories.html',context={"item":item})


def view_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart = Cart.objects.get(user=user)
        # print(cart)
        cart_items = CartItems.objects.filter(cart=cart)
        sum_of_cost = []
        for c in cart_items:
            sum_of_cost.append(c.total_cost())
        total_price = sum(sum_of_cost)
        shiping = 60
        payable_amt = total_price+shiping
        return render(request,'cart.html',context={"cart":cart_items,"total_price":total_price,"shiping":shiping,"amount":payable_amt})


def add_cart(request,uuid):
    if request.user.is_authenticated:
        user = request.user
        item = Product.objects.get(uuid=uuid)
        cart,created = Cart.objects.get_or_create(user=user)
        cart_items,created = CartItems.objects.get_or_create(cart=cart,product=item)
        # print(cart_items)
        if not created:
        # If the cart item already exists, just increment the quantity
            cart_items.quantity += 1
            cart_items.save()
        return redirect('view_cart')
    else:
        return redirect('login')

def remove_item_cart(request):
    return render(request,'cart.html')

def get_product_view(request,uuid):
    # print(uuid)
    item = Product.objects.get(uuid=uuid)
    # print(item)
    return render(request,'get_product_view.html',context={"item":item})
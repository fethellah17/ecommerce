from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
import datetime
from .models import Product, Category, Order, OrderItem, ShippingAddress, Wishlist
from .forms import ShippingForm, DELIVERY_PRICES


def store(request):
    category_id = request.GET.get('category')
    sale_filter = request.GET.get('sale')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    elif sale_filter == 'true':
        products = Product.objects.filter(is_sale=True)
    else:
        products = Product.objects.all()

    # Get cart items count and wishlist
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        cartItems = order.get_cart_items
        wishlist_items = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
        wishlist_count = wishlist_items.count()
    else:
        cartItems = 0
        wishlist_items = []
        wishlist_count = 0

    context = {
        'products': products,
        'categories': categories,
        'cartItems': cartItems,
        'sale_filter': sale_filter,
        'wishlist_items': wishlist_items,
        'wishlist_count': wishlist_count,
    }
    return render(request, 'store/store.html', context)


@login_required
def cart(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = 0

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to checkout')
        return redirect('login')

    order, created = Order.objects.get_or_create(user=request.user, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    if cartItems == 0:
        messages.warning(request, 'Your cart is empty')
        return redirect('store')

    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.user = request.user
            shipping.order = order
            shipping.save()

            # Get shipping cost based on wilaya
            state_code = form.cleaned_data.get('state')
            shipping_cost = DELIVERY_PRICES.get(state_code, 0)
            
            # Complete the order
            order.shipping_cost = shipping_cost
            order.complete = True
            order.transaction_id = datetime.datetime.now().timestamp()
            order.save()

            messages.success(request, 'Order placed successfully!')
            return redirect('order_complete')
    else:
        form = ShippingForm()

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'form': form,
    }
    return render(request, 'store/checkout.html', context)


def order_complete(request):
    return render(request, 'store/order_complete.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:4]
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        cartItems = order.get_cart_items
        is_in_wishlist = Wishlist.objects.filter(user=request.user, product=product).exists()
        wishlist_count = Wishlist.objects.filter(user=request.user).count()
    else:
        cartItems = 0
        is_in_wishlist = False
        wishlist_count = 0
    
    context = {
        'product': product,
        'related_products': related_products,
        'cartItems': cartItems,
        'is_in_wishlist': is_in_wishlist,
        'wishlist_count': wishlist_count,
    }
    return render(request, 'store/product_detail.html', context)


def main(request):
    return render(request, 'store/main.html')


@login_required
def update_cart(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to update cart')
        return redirect('login')

    if request.method == 'POST':
        productId = request.POST.get('productId')
        action = request.POST.get('action')
        size = request.POST.get('size', '')

        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        
        # For products with sizes, match by product AND size
        if product.has_sizes and size:
            orderItem, created = OrderItem.objects.get_or_create(
                order=order, product=product, size=size
            )
        else:
            orderItem, created = OrderItem.objects.get_or_create(
                order=order, product=product, size=''
            )

        if action == 'add':
            orderItem.quantity += 1
        elif action == 'remove':
            orderItem.quantity -= 1

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

    # Redirect back to referring page or cart
    referer = request.META.get('HTTP_REFERER', '')
    if 'cart' in referer:
        return redirect('cart')
    return redirect('store')


@login_required
def delete_cart_item(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please login')
        return redirect('login')

    if request.method == 'POST':
        itemId = request.POST.get('itemId')
        try:
            orderItem = OrderItem.objects.get(id=itemId, order__user=request.user, order__complete=False)
            orderItem.delete()
            messages.success(request, 'Item removed from cart')
        except OrderItem.DoesNotExist:
            messages.error(request, 'Item not found')

    return redirect('cart')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('store')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'store/login.html', {'form': form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('store')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()

    return render(request, 'store/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('store')


@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    
    context = {
        'wishlist_items': wishlist_items,
        'cartItems': cartItems,
    }
    return render(request, 'store/wishlist.html', context)


@login_required
def toggle_wishlist(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            wishlist_item, created = Wishlist.objects.get_or_create(
                user=request.user, 
                product=product
            )
            
            if not created:
                wishlist_item.delete()
                is_in_wishlist = False
                messages.success(request, f'{product.name} removed from favorites')
            else:
                is_in_wishlist = True
                messages.success(request, f'{product.name} added to favorites')
            
            # Return JSON response for AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'is_in_wishlist': is_in_wishlist,
                    'message': f'{product.name} {"added to" if is_in_wishlist else "removed from"} favorites'
                })
                
        except Product.DoesNotExist:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Product not found'})
            messages.error(request, 'Product not found')
    
    # Redirect back to referring page
    return redirect(request.META.get('HTTP_REFERER', 'store'))
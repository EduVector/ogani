from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from apps.product.models import Product
from .models import Cart, CartItem, WishList, Order


def add_to_cart(request):
    url = request.META.get('HTTP_REFERER')
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('quantity')  # maxsulotning soni
    session_id = request.session.session_key
    ip_address = request.META.get('REMOTE_ADDR')
    print(product_id, quantity)
    cart = Cart.objects.filter(session_id=session_id, is_completed=False).first()
    product = Product.objects.get(id=int(product_id))
    if cart:
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if cart_item:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)
    else:
        cart = Cart.objects.create(session_id=session_id, ip_address=ip_address)
        CartItem.objects.create(cart=cart, product=product, quantity=quantity)
    return redirect(url)


def add_to_wish_list(request, pk):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(product_id=pk, user=request.user).first()
        if wishlist:
            wishlist.delete()
        else:
            WishList.objects.create(product_id=pk, user=request.user)
    else:
        wishlist = WishList.objects.filter(product_id=pk, session_id=request.session.session_key).first()
        if wishlist:
            wishlist.delete()
        else:
            WishList.objects.create(product_id=pk, session_id=request.session.session_key)
    return redirect(url)


def cart(request):
    cart = Cart.objects.filter(session_id=request.session.session_key, is_completed=False).first()
    cart_items = CartItem.objects.filter(cart=cart, order=None, is_active=True)

    context = {
        "cart": cart,
        "cart_items": cart_items
    }
    return render(request, 'cart.html', context)


def remove_from_cart(request, pk):
    url = request.META.get('HTTP_REFERER')
    cart_item = CartItem.objects.get(id=pk)
    cart_item.delete()
    return redirect(url)


@login_required
def create_order(request):
    cart = Cart.objects.filter(session_id=request.session.session_key, is_completed=False).first()
    cart_items = CartItem.objects.filter(cart_id=cart.id, order=None, is_active=True)
    order = Order.objects.create(user=request.user)
    for item in cart_items:
        item.order = order
        item.save()
    cart.is_completed = True
    cart.save()
    return redirect('checkout')


@login_required
def checkout(request):
    full_name = request.POST.get('full_name', None)
    phone = request.POST.get('phone', None)
    notes = request.POST.get('notes', None)
    order = Order.objects.filter(user=request.user).last()
    if request.method == 'POST':
        order.full_name = full_name
        order.phone = phone
        order.notes = notes
        order.save()
        return redirect('home')

    context = {
        "order": order
    }
    return render(request, 'checkout.html', context)


def wishlist(request):
    wishlist = WishList.objects.filter(session_id=request.session.session_key)
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(Q(user=request.user) | Q(session_id=request.session.session_key))
    context = {
        "wishlist": wishlist
    }
    return render(request, 'wishlist.html', context)

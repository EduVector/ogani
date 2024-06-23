from django.contrib import admin
from apps.order.models import Order, Cart, CartItem, WishList


admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(WishList)

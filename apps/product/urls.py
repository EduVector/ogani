from django.urls import path
from .views import home, shop_detail, shop

urlpatterns = [
    path('', home, name="home"),
    path('shop/detail/<slug:slug>/', shop_detail, name="detail"),
    path('shop', shop, name="shop"),
]
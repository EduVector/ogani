from django.urls import path
from .views import home, shop_detail

urlpatterns = [
    path('', home, name="home"),
    path('shop/detail/<int:pk>/', shop_detail, name="detail"),
]
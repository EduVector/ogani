from django.urls import path
from apps.product.views import index, shop_detail


urlpatterns = [
    path('', index, name='index'),
    path('shop/detail/<int:pk>/', shop_detail, name="detail"),
]

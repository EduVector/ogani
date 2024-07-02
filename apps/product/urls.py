from django.urls import path
from apps.product.views import index, shop_detail
from apps.blog.views import blog_detail


urlpatterns = [
    path('', index, name='index'),
    path('shop/detail/<int:pk>/', shop_detail, name="detail"),
    path('blog-single/<slug:slug>/', blog_detail, name='blog-detail'),
]

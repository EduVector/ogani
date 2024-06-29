from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Banner, Category, Product


def home(request: Any) -> Any:
    banners = Banner.objects.all().last()
    categories = Category.objects.filter(parent__isnull=False)
    products = Product.objects.all()
    context = {
        'banner': banners,
        'categories': categories, 
        'products': products
    }
    return render(request, 'index.html', context)
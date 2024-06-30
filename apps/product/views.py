from django.shortcuts import render
from .models import Banner, Category, Product
from apps.blog.models import Article


def home(request):
    banners = Banner.objects.all()
    parent = banners.filter(parent__isnull=True).last()
    categories = Category.objects.all().order_by('name')
    products = Product.objects.all()
    last_products = products.order_by('-id')[:6]
    top_reted_products = products.order_by('-id')[:6]
    review_products = products.order_by('-id')[:6]
    articles = Article.objects.all()

    context = {
        'banner': parent,
        'last_two_banners': banners.filter(parent=parent),
        'categories': categories, 
        'products': products.order_by('?')[:9],
        'last_products': last_products,
        'top_reted_products': top_reted_products,
        'review_products': review_products,
        'articles': articles[:3]
    }
    return render(request, 'index.html', context)


def shop_detail(request, pk):
    product = Product.objects.filter(id=pk).first()
    return render(request, 'detail.html', {"product": product})

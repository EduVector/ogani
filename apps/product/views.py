from django.shortcuts import render
from .models import Banner, Category, Product
from apps.blog.models import Article
from django.db.models import Q
from django.core.paginator import Paginator


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


def shop_detail(request, slug):
    product = Product.objects.filter(slug__iexact=slug).first()
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'detail.html', context)


def shop(request):
    page = request.GET.get('page')
    products = Product.objects.all()
    sale_products = products.order_by('-percentage').exclude(Q(percentage=None) | Q(percentage=0))[:6]

    paginator = Paginator(products, 1)
    selected_page = paginator.get_page(page)
    context = {
        'products': products.order_by('?')[:9],
        'sale_products': sale_products,
        'object_list': selected_page
    }
    return render(request, 'shop.html', context)

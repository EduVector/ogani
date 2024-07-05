from django.shortcuts import render
from apps.blog.models import Category, Tag, Blog


def blog(request):
    # tag = request.GET.get('tag')
    # cat = request.GET.get('cat')

    blogs = Blog.objects.all().order_by('-id')[:6]
    recent_blogs = Blog.objects.all().order_by('-id')[:3]
    tags = Tag.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')


    # if tag:
    #     blogs = blogs.filter(tags__slug__exact=tag)

    # if cat:
    #     blogs = blogs.filter(category__slug__exact=cat)

    context = {
        'blogs': blogs,
        'tags': tags,
        'recent_blogs': recent_blogs,
        'category': categories,

    }

    return render(request, 'blog.html', context)

def blog_detail(request, slug):
    # tag = request.GET.get('tag')
    # cat = request.GET.get('cat')

    blog = Blog.objects.get(slug__exact=slug)

    blogs = Blog.objects.all().order_by('-id')[:3]

    # if tag:
    #     blogs = blogs.filter(tags__slug__exact=tag)

    # if cat:
    #     blogs = blogs.filter(category__slug__exact=cat)    

    context = { 
        'blog': blog,
        'blogs': blogs,
    }

    return render(request, 'blog-detail.html', context)

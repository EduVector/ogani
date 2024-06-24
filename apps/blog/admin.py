from django.contrib import admin
from apps.blog.models import Tag, Category, Blog


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Blog)

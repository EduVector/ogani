from django.contrib import admin
from apps.blog.forms import ArticleAdminForm
from apps.blog.models import Article, Category, Tag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('id', 'name', 'category',  'created_at')


admin.site.register(Category)
admin.site.register(Tag)
from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category, Tag


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


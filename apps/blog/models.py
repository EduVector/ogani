from django.db import models
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField


class Category(BaseModel):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name


class Article(BaseModel):
    name = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to="artices/", null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

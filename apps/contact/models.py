from django.db import models
from apps.common.models import BaseModel


class ContactUs(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
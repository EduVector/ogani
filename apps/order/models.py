from django.db import models
from apps.common.models import BaseModel
from apps.product.models import Product
from django.contrib.auth.models import User

STATUS = (
    (0, 'New'),
    (1, 'Completed'),
    (2, 'Canceled'),
)

class Order(BaseModel):
    status = models.IntegerField(choices=STATUS, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="orders")
    
    @property
    def total(self):
        return sum([item.total for item in self.items.all()])
    
    def __str__(self):
        return f'{self.user.username} - {self.status}'


class Cart(BaseModel):
    is_completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.session_id


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total(self):
        return self.product.discount * self.quantity

    def __str__(self):
        return f'{self.product.name}'

class WishList(BaseModel):
    session_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

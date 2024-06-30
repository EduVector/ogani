from apps.product.models import Category
from apps.order.models import WishList, CartItem

def objects(request):
    categories = Category.objects.all()
    wishlist_count = WishList.objects.all().count()

    return {
        "categories": categories,
        "wishlist_count": wishlist_count
    }

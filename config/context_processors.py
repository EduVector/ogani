from apps.product.models import Category
from apps.order.models import WishList, CartItem

def objects(request):
    categories = Category.objects.all().order_by('name')
    wishlist_count = 0
    if request.user.is_authenticated:
        wishlist_count = WishList.objects.filter(user=request.user).count()

    return {
        "categories": categories,
        "wishlist_count": wishlist_count
    }

from core.models import *



def default(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, active=True).first()
        item_count = cart.cartitem_set.count() if cart else 0
    else:
        item_count = 0

    context = {
        'categories': categories,
        'cart_view': {'item_count': item_count},
    }
    return context
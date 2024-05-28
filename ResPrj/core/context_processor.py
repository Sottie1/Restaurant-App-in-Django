from core.models import *



def default(request):
    categories = Category.objects.all()

    context = {
        'categories':categories,
    }
    return context
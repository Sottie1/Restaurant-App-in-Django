from django.shortcuts import render
from core.models import *
from django.shortcuts import get_object_or_404, redirect, render
from core.models import *
from .forms import contactForm,MenuReviewForm
from django.contrib.auth.decorators import login_required
import uuid
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST



# Create your views here.


def home(request):
	menu_item = MenuItem.objects.filter(item_status = "published", featured = True, recent=False).order_by('-id')
	recent_item = MenuItem.objects.filter(item_status="published", recent=True).order_by('-id')

	context = {
		'menu_item':menu_item,
		'recent_item':recent_item,
	}
	return render(request, "core/index.html", context)



def menu(request):

	menu_list = MenuItem.objects.filter(item_status = "published").order_by('-id')

	context = {
		'menu_list':menu_list 
	}
	return render(request, "core/menu.html", context)


def menu_detail(request, mid):
	menud = MenuItem.objects.get(mid=mid)
	m_image =  menud.m_images.all()
	menus = MenuItem.objects.filter(category=menud.category).exclude(mid=mid)
	reviews = Review.objects.filter(menu_item=menud)
	form = MenuReviewForm()

	make_review = True

	
	context = {
		'menud':menud,
		'm_images':m_image,
		'menus':menus,
		'reviews':reviews,
		'form':form,
		'make_review':make_review,
	}
	return render(request, "core/menu_detail.html", context)



def add_to_cart(request, item_id):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to be logged in to add items to the cart.")
        return redirect('userauths:login')  

    menu_item = get_object_or_404(MenuItem, mid=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user, active=True)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Item added to cart successfully.")
    return redirect('core:cart_view')

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user, active=True)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'core/cart.html', context)

@login_required
@require_POST
def update_cart_item(request, item_id):
    data = json.loads(request.body)
    delta = data.get('delta', 0)
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user, cart__active=True)
    if cart_item.quantity + delta > 0:
        cart_item.quantity += delta
        cart_item.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})



@login_required
@require_POST
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user, cart__active=True)
    cart_item.delete()
    return JsonResponse({'success': True})





@login_required
def submit_review(request, mid):
    menu_item = get_object_or_404(MenuItem, mid=mid)
    if request.method == 'POST':
        form = MenuReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.menu_item = menu_item
            review.save()
            return redirect('core:menu_detail', mid=mid)
    else:
        form = MenuReviewForm()

    reviews = Review.objects.filter(menu_item=menu_item)
    context = {
        'form': form,
        'make_review': True,
        'reviews': reviews,
        'menud': menu_item,
    }
    return render(request, 'core/menu_detail.html', context)

def CategoryList(request):
	categories = Category.objects.all()

	context = {
		'categories':categories,
	}
	return render(request, "core/category_list.html", context)



def category_menu_list(request, cid):
    category = get_object_or_404(Category, cid=cid)
    menuIt = MenuItem.objects.filter(item_status="published",category=category)

    context = {
        'category': category,
        'menuIt': menuIt,
    }

    return render(request, "core/category_menu_list.html", context)



def aboutUs(request):

	return render(request, "core/about.html")



def online_order(request):
	return render(request, "core/online_order.html")


def login(request):
	return render(request, "core/login.html")


def signup(request):

	return render(request, "core/signup.html")



def contactUs(request):
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('core:success')
		
	else:
		form = contactForm()
	return render(request, "core/contact.html", {'form':form})



    
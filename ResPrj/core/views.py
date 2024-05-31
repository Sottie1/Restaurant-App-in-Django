from django.shortcuts import render
from core.models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from core.models import *
from django.template.loader import render_to_string
from django.urls import reverse
from .forms import contactForm,MenuReviewForm
from django.contrib.auth.decorators import login_required



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

	# review = MenuReview.objects.filter(menud=menud).order_by('-date')
	# review_form = MenuReviewForm()
	# make_review = True
	# user_review_count = 0

	# if request.user.is_authenticated:
	# 	user_review_count = MenuReview.objects.filter(user=request.user, MenuItem=menud).count()

	# if user_review_count > 0:
	# 	make_review = False


	context = {
		'menud':menud,
		'm_images':m_image,
		'menus':menus,
		# 'review':review,
		# 'make_review':make_review,
		# 'review_form':review_form,
	}
	return render(request, "core/menu_detail.html", context)

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = MenuReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('core:menu_detail') 
    else:
        form = MenuReviewForm()
    
    context = {
        'form': form,
        'make_review': True
    }
    return render(request, 'core/menu_detail.html', context)

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = MenuReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')  # Redirect to a success page or the same page
    else:
        form = MenuReviewForm()
    
    reviews = MenuReview.objects.all()  # Fetch all reviews or filter based on criteria
    context = {
        'form': form,
        'make_review': True,
        'reviews': reviews,
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



    
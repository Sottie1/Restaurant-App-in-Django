from django.shortcuts import render
from core.models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from core.models import *
from django.template.loader import render_to_string
from django.urls import reverse
from .forms import contactForm


# Create your views here.


def home(request):
	menu_item = MenuItem.objects.filter(item_status = "published", featured = True).order_by('-id')

	context = {
		'menu_item':menu_item,
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

	context = {
		'menud':menud,
		'm_images':m_image,
	}


	return render(request, "core/menu_detail.html", context)

def CategoryList(request):
	categories = Category.objects.all()

	context = {
		'categories':categories,
	}
	return render(request, "core/category_list.html", context)

from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem

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



    
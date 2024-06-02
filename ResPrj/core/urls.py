from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from django.views.generic import TemplateView


app_name = 'core'

urlpatterns = [
	path("", home, name="home"),
    
	path("menu/", menu, name="menu"),
	path("menu/<uuid:mid>/", menu_detail, name="menu_detail"),
    
	path("about/", aboutUs, name="aboutUs"),
    
    path('category_list/', CategoryList, name="categoryList"),
    path('category_menu_list/<cid>/', category_menu_list, name="category_menu_list"),
    
    path('submit-review/<uuid:mid>/', submit_review, name='submit_review'),
    
	############## Cart ##############
    path("add_to_cart/<uuid:mid>/", add_to_cart, name="add_to_cart"),
	
    
	path("login/", login, name="login"),
	path("signup/", signup, name="signup"),
    
	path("contact/", contactUs, name="contactUs"),
   
    
]

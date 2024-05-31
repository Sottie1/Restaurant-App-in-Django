from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from django.views.generic import TemplateView


app_name = 'core'

urlpatterns = [
	path("", home, name="home"),
    
	path("menu/", menu, name="menu"),
	path("menu/<mid>/", menu_detail, name="menu_detail"),
    
	path("about/", aboutUs, name="aboutUs"),
    
    path('category_list/', CategoryList, name="categoryList"),
    path('category_menu_list/<cid>/', category_menu_list, name="category_menu_list"),
    
    path('submit-review/', submit_review, name='submit_review'),
    
	path("online_order/", online_order, name="online_order"),
    
	path("login/", login, name="login"),
	path("signup/", signup, name="signup"),
    
	path("contact/", contactUs, name="contactUs"),
    path('success/', TemplateView.as_view(template_name="core/success.html"), name='success'),
    
]

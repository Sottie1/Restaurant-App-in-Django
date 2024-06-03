from django.contrib import admin
from core.models import *

# Register your models here.

class MenuImagesAdmin(admin.TabularInline):
    model = MenuImages


class MenuItemsAdmin(admin.ModelAdmin):
    inlines = [MenuImagesAdmin]
    list_display = ['title', 'image', 'price', ]

class cartAdmin(admin.ModelAdmin):
     list_display= ['user', 'active']


class CartItemAdmin(admin.ModelAdmin):
     list_display = ['cart', 'menu_item', 'quantity']

class OrderAdmin(admin.ModelAdmin):
     list_display = ['user', 'total_price', 'status', 'created_at']

class OrderItemAdmin(admin.ModelAdmin):
     list_display = ['order', 'quantity', 'price']

class contactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone', 'subject', 'message']

class CategoryAdmin(admin.ModelAdmin):
     list_display = ['title', 'image']

class ReviewsAdmin(admin.ModelAdmin):
     list_display = ['name', 'email', 'text', 'rating']







admin.site.register(MenuItem, MenuItemsAdmin)
admin.site.register(Cart, cartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(contact, contactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewsAdmin)
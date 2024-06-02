from django.contrib import admin
from core.models import *

# Register your models here.

class MenuImagesAdmin(admin.TabularInline):
    model = MenuImages


class MenuItemsAdmin(admin.ModelAdmin):
    inlines = [MenuImagesAdmin]
    list_display = ['title', 'image', 'price', ]

class cartAdmin(admin.ModelAdmin):
     pass
    

class contactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone', 'subject', 'message']

class CategoryAdmin(admin.ModelAdmin):
     list_display = ['title', 'image']

class ReviewsAdmin(admin.ModelAdmin):
     list_display = ['name', 'email', 'text', 'rating']







admin.site.register(MenuItem, MenuItemsAdmin)
admin.site.register(contact, contactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewsAdmin)
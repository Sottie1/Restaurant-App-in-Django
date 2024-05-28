from django.contrib import admin
from core.models import *

# Register your models here.

class MenuImagesAdmin(admin.TabularInline):
    model = MenuImages


class MenuItemsAdmin(admin.ModelAdmin):
    inlines = [MenuImagesAdmin]
    list_display = ['title', 'image', 'price', ]
    

class contactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'phone', 'subject', 'message']

class CategoryAdmin(admin.ModelAdmin):
     list_display = ['title', 'image']





admin.site.register(MenuItem, MenuItemsAdmin)
admin.site.register(contact, contactAdmin)
admin.site.register(Category, CategoryAdmin)
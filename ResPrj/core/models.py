from django.db import models
from shortuuid.django_fields import ShortUUIDField
import uuid
from userauths.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


# Create your models here.


STATUS = (
    ("draft", "Draft"),
    ("diabled", "Disabled"),
    ("rejected","Rejected"),
    ("in_review","In Review"),
    ("published","Published"),
)

RATINGS =[
   
    (1, "✮☆☆☆☆"),
    (2, "✮✮☆☆☆"),
    (3, "✮✮✮☆☆"),
    (4, "✮✮✮✮☆"),
    (5, "✮✮✮✮✮"),
]

STATUS_CHOICES = (
    ("processing", "Processing"),
    ("shipped", "Shipped"),
    ("delivered","Delivered"),
)

class Category(models.Model):
    cid = models.UUIDField(default=uuid.uuid4, editable=False, unique = True )
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="category_Images/")
    description = models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural ="Categories"

    def category_image(self):
        return mark_safe('<img src= "%s" width = "50", height="50"/>' % (self.image.url))

    def __str__(self):
        return self.title
    
    
class MenuItem(models.Model):
    mid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    title = models.CharField(max_length=200)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, related_name="category")
    image = models.ImageField(upload_to="menu_Images/")
    price = models.DecimalField(max_digits=9, decimal_places=2, default="0.00")
    item_status = models.CharField(choices=STATUS, max_length=100, default="in_review")
    featured = models.BooleanField(default=False)
    recent = models.BooleanField(default=False)
    description = RichTextUploadingField(null=True, blank=True)
    specification = RichTextUploadingField(null= True, blank = True)

    def __str__(self):
        return self.title
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='CartItem')
    active = models.BooleanField(default=True)

    def add_item(self, menu_item):
        cart_item, created = CartItem.objects.get_or_create(cart=self, menu_item=menu_item)
        if not created:
            cart_item += 1
            cart_item.save()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.CharField(choices = STATUS_CHOICES, max_length=20)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2)



class MenuImages(models.Model):
    images = models.ImageField(upload_to = "menu_sub_images")
    menuIt = models.ForeignKey(MenuItem, related_name = 'm_images', on_delete = models.SET_NULL, null = True )
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural= "Menu Sub Images" 

    def menu_image(self):
        return mark_safe('<img src= "%s" width = "50", height="50"/>' % (self.image.url))
    





class Review(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    rating = models.IntegerField(choices=RATINGS, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review by {self.name} on {self.menu_item}'



class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
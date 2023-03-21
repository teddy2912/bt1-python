from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null= True, blank=True)

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null= True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()
    

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")

class Customer(BaseModel):
    user= models.OneToOneField(User,on_delete=models.SET_NULL,null=True, blank=False)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    
class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)
    complate = models.BooleanField(default=False,null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
   
class OrderDetail(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
class ShippingAdress(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    
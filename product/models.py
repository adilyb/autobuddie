from distutils.command.upload import upload
from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class ProductModel(models.Model):
    name =  models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='images/product',default='')
    price = models.DecimalField( max_digits=10, decimal_places=2, blank=True,null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    description = models.TextField(max_length=2300, blank=True,null=True)
    uploaded_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def _str_(self) -> str:
        return self.name
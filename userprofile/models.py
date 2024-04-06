from django.db import models 
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
        ('Other','Other')
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    age = models.IntegerField( blank=True, null=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    house_name = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    postoffice = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username
    
        
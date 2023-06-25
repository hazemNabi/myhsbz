from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models  import Token
from django.conf import settings
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.db.models import Sum, F
from multiselectfield import MultiSelectField
# from django.dispatch import receiver


class TypeAccount(models.Model):
    nameType=models.CharField(max_length=15,null=True,blank=True)
    desc=models.CharField(max_length=50,blank=False)
    photo=models.ImageField(upload_to='photos',null=True)

    def __str__(self):
        return self.nameType



class CustomUser(AbstractUser):
    TypeUser=models.ForeignKey(TypeAccount,null=True,on_delete=models.CASCADE,verbose_name='نوع الحساب')
    photo=models.ImageField(upload_to='photos',null=True, default='')
    PhonNumber=models.CharField(max_length=16,blank=False,null=True,verbose_name='رقم الموبايل')
    emp_company= models.IntegerField(blank=False,null=True) 
    is_busy = models.BooleanField(default=False)
    username = models.CharField(verbose_name='اسم المستخدم', max_length=150, unique=True)
    password = models.CharField(verbose_name='كلمة المرور', max_length=128)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    related_name="coustmer"
    class Meta:
        verbose_name = 'المستخدم'
        verbose_name_plural = 'المستخدمين'
        verbose_name = ' المرور'
        verbose_name_plural = ' يالمرور'
   
    REQUIRED_FIELDS = []
    # def create_user(self, username, password, **extra_fields):
    #     """
    #     Create and save a User with the given email and password.
    #     """
    #     if not username:
    #         raise ValueError(("The username must be set"))
    #     username = self.normalize_username(username)
    #     # PhonNumber = self.normalize_phonumber(PhonNumber)

    #     coustmer = self.model(username=username, **extra_fields)
    #     coustmer.set_password(password)
    #     coustmer.save()
    #     return coustmer
    def register(self):
        self.save()
    def __str__(self):
        return self.username




class Address(models.Model):
    address_coustem_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="address")
    addressType = models.CharField(max_length=250,  blank=True)
    contacktPersonNumber = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100,  blank=True)
    address_latitude = models.CharField(max_length=50, blank=True) 
    address_longitude = models.CharField(max_length=50,  blank=True)  
    def __str__(self):
        return self.address


class employees(models.Model):
    name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=10, blank=True) 
    address = models.CharField(max_length=40,blank=True)
    is_active = models.BooleanField(default=True)
    emp_company =  models.ForeignKey(CustomUser,on_delete=models.CASCADE)













   
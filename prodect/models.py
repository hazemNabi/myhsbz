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
from account.models import CustomUser

class CoustemSections(models.Model):
     name=models.CharField(max_length=30,blank=False,)
     desc=models.CharField(max_length=50,blank=False,)
     Coustmer_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=False, related_name="coustmerSections")
     def __str__(self):
        return self.name


class Products(models.Model):
    namepasnes=models.CharField(max_length=20,null=True,blank=False,help_text="الاسم التجاري")
    namescient=models.CharField(max_length=20,null=True,blank=False,help_text="الاسم العلمي")
    manufactureCompany=models.CharField(max_length=20,null=True,blank=False,help_text="الشركة المصنعة")
    desc=models.CharField(max_length=10,blank=False,help_text="وصف المنتج")
    quntity=models.CharField(max_length=10,blank=False,help_text="كمية المنتج")
    Created_at=models.DateField(max_length=20,blank=False,help_text="تاريخ انشاء المنتج")
    dataFinshProdect=models.DateField(max_length=20,blank=False,help_text="تارخ انتهاء المنتج")
    photo=models.ImageField(upload_to='photos',null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    coustemCatogry=models.ForeignKey(CoustemSections,on_delete=models.CASCADE,blank=False,related_name='products')
    prodect_CoustmerId=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=False,related_name='products')
    def __str__(self):
        return self.namepasnes

class productOffers(models.Model):
    nameOffers=models.CharField(max_length=20,blank=False,help_text="اسم العرض")
    offers_prodectIid=models.ForeignKey(Products,on_delete=models.CASCADE,blank=False,)
    quntity_of_start_Offers=models.CharField(max_length=10,blank=False,help_text="كمية")
    amount_increase=models.CharField(max_length=10,blank=False,help_text=" كمية الزيادة")
    price_with_increase=models.FloatField(max_length=10,null=True,blank=False,help_text=" سعر البيع مع العرض")
# class SearchModel(models.Model):
#     namepasnes=models.CharField(max_length=20,null=True,blank=False,help_text="الاسم التجاري")
#     namescient=models.CharField(max_length=20,null=True,blank=False,help_text="الاسم العلمي")
#     photo=models.ImageField(upload_to='photos',null=True)
#     price = models.DecimalField(max_digits=6,decimal_places=2)
#     price_with_increase=models.FloatField(max_length=10,null=True,blank=False,help_text=" سعر البيع مع العرض")
#     prodect_CoustmerId=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=False,related_name='products')



















   
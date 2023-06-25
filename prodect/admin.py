from django.contrib import admin

# Register your models here.


# Register your models here.
from prodect.models import *

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin







# admin.site.register(Prodect)
admin.site.register(CoustemSections)
admin.site.register(productOffers)
admin.site.register(Products)




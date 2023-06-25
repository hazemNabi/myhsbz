from django.contrib import admin

# Register your models here.
from account.models import *

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,employees,TypeAccount,Address



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # list_display = ['password', 'username']


admin.site.register(CustomUser)
admin.site.register(TypeAccount)



admin.site.register(employees)
admin.site.register(Address)



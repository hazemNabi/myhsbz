from django import forms
from .models import *
from django.contrib.auth import get_user_model

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','TypeUser','PhonNumber')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model =CustomUser
        fields = ('username','email', 'TypeUser','PhonNumber')


class addCoustmer(forms.ModelForm):
  
   
    class Meta:
        model =CustomUser
        fields = {'username','email','password', 'TypeUser'}
        widgets={
           'username':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'password':forms.PasswordInput(attrs={'class':'form-control pull-right'},),
           'email':forms.EmailInput(attrs={'class':'form-control pull-right'},),
           'TypeUser':forms.Select(attrs={'class':'form-control pull-right'},),
         }
class EemployeeCreationForm(UserCreationForm):
    class Meta:
        model =CustomUser
        fields = ('username','TypeUser','PhonNumber')

class addEmployee(forms.ModelForm):
  
   
    class Meta:
        model =CustomUser
        fields = {'username','password', 'TypeUser'}
        widgets={
           'username':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'password':forms.PasswordInput(attrs={'class':'form-control pull-right'},),
           'TypeUser':forms.Select(attrs={'class':'form-control pull-right'},),
         }




        
class proFiel(forms.ModelForm):
    class Meta:
        model =CustomUser
        fields = ['username','password','photo','email','first_name','last_name']
        
        widgets={
           'username':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'password':forms.PasswordInput(attrs={'class':'form-control pull-right'},),
           'email':forms.EmailInput(attrs={'class':'form-control pull-right'},),
           'photo':forms.FileInput(attrs={'class':'form-control pull-right'},),
           'first_name':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'last_name':forms.TextInput(attrs={'class':'form-control pull-right'},),
        }




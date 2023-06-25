from django import forms
from prodect.models import *
from django.contrib.auth import get_user_model

from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm








class addProdect(forms.ModelForm):

    # coustemCatogry=forms.Select(attrs={'class':'form-control pull-right'},)
    class Meta:
        model =Products
        fields = ['namepasnes','namescient','manufactureCompany','photo','coustemCatogry','desc','dataFinshProdect','Created_at','quntity', 'price']
        
        widgets={
           'namepasnes':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'namescient':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'manufactureCompany':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'photo':forms.FileInput(attrs={'class':'form-control pull-right'},),
           'coustemCatogry':forms.Select(attrs={'class':'form-control pull-right'},),
           'desc':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'dataFinshProdect':forms.DateInput(format='%Y-%m-%d'),
           'Created_at':forms.DateInput(format='%Y-%m-%d'),
           'quntity':forms.NumberInput(attrs={'class':'form-control pull-right'},),
           'price':forms.NumberInput(attrs={'class':'form-control pull-right'},),
           

        }
        


class addSections(forms.ModelForm):
    class Meta:
        model =CoustemSections
        fields = ['name','desc']
        
        widgets={
           'name':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'desc':forms.TextInput(attrs={'class':'form-control pull-right'},),
        }
        

class productOffer(forms.ModelForm):
    class Meta:
        model =productOffers
        fields = ['nameOffers','quntity_of_start_Offers','amount_increase']
        
        widgets={
           'nameOffers':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'quntity_of_start_Offers':forms.NumberInput(attrs={'class':'form-control pull-right'},),
           'amount_increase':forms.NumberInput(attrs={'class':'form-control pull-right'},),
        }
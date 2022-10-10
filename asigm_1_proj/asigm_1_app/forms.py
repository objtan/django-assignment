from django.forms import ModelForm
from .models import Person
from django import forms

# class AddUserForm(forms.Form):
#     name =  forms.CharField(label='Full Name', max_length=100)
#     age = forms.IntegerField(label='Age', required=False)
#     address = forms.CharField(label='Address', max_length=200)
#     mobile_number = forms.CharField(label='Phone Number', max_length=50)


class AddUserForm(ModelForm):
    class Meta:
        model=Person
        fields = ['name','age','address','mobile_number']  

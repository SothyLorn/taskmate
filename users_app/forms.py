from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name= forms.CharField(max_length=30,label='First Name')
    last_name= forms.CharField(max_length=30,label='Last Name')
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
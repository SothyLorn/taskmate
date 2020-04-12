from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = CustomerRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("User Created Successfully !!!"))
            return redirect('register')
            
    else: 
        register_form = CustomerRegisterForm()  
    return render(request,'register.html', {'register_form': register_form })
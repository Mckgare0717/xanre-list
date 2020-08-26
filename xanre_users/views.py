from django.shortcuts import render,redirect
from .forms import customregisterforms
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        register_form = customregisterforms(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("new user account created, login to get in"))
            return redirect('register')



    else:
        register_form = customregisterforms()
    return render(request , 'register.html' , {'register_form':  register_form})
   

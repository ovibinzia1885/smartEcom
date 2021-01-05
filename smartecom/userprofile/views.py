from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate, login
from django.contrib import messages
from ecom.models import Setting
from .forms import SignUpForm
from product.models import Product,Images,Category


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        # Redirect to a success page.
        else:
            messages.warning(request,'please valid username password')
    product_catagory = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={
        'setting':setting,
        'product_catagory':product_catagory,

    }
    return render(request,'user_login.html',context)





def user_logout(request):
    logout(request)
    return  redirect('home')

def user_register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password_raw=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password_raw)
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'you reset password is not matching')
    else:
        form=SignUpForm()
    product_catagory = Category.objects.all()
    setting = Setting.objects.get(id=1)
    context={
        'form':form,
        'setting': setting,
        'product_catagory': product_catagory,
    }
    return render(request,'user_register.html',context)

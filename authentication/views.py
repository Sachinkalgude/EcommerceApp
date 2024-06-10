from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib import messages
# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignUpForm()
            return redirect('login')
        else:
            form = SignUpForm()
            return redirect("signup")
        
    return render(request,'signup.html',context={"form":form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # This field captures the email in your form
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        form  = SignUpForm(instance=request.user)
        return render(request,'profile.html',context={"form":form})
    else:
        return redirect('login')
        

def logoutView(request):
        logout(request)
        return redirect('login')
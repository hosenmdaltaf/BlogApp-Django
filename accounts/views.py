from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm     #UserCreationForm,
from django.contrib.auth import login,logout

from django.contrib import messages
from .forms import UserRegisterForm

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has created ! You are now able to log in')
            return redirect ('accounts:login')
    else:
        form =UserRegisterForm()
    return render (request,'accounts/signup.html',{'form':form})

# def signup(request):
#     #user register form
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#            user = form.save()
#             #log in user
#            login(request,user)
#            return redirect('accounts:login')
#     else:
#         form=UserCreationForm()

#     return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user=form.get_user()
            login(request,user)
            return redirect('blogapp:home')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:logout')
    return render(request,'accounts/logout.html')




from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup(request):
    #user register form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
            #log in user
           login(request,user)
           return redirect('accounts:login')
    else:
        form=UserCreationForm()

    return render(request,'accounts/signup.html',{'form':form})

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
        return redirect('blogapp:logout')
    return render(request,'blogapp/logout.html')




from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post 

#def home(request):
    #blog=Blog.objects.all()
    #return render (request,'blogapp/blog.html',{'blogs':blog})

class HomeView(ListView):
    model=Post
    template_name='blogapp/blog.html'
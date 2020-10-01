from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post 
from .import views

'''
import requests
from bs4 import BeautifulSoup
import lxml

def home(request):
    blog=Post.objects.all()
    obj=Post.objects.get(id=pk) 
    ordering=['-date']
    return render (request,'blogapp/blog.html',{'blog':blog})
    '''

class HomeView(ListView):
    # model=Post
    # obj=Post.objects.order_by(-id)[0]
    #obj= Post.objects.filter().order_by('-id')[0]

    def get_queryset(self):
        return Post.objects.all().order_by('-id')

    ordering=['-date']
    template_name='blogapp/blog.html'

class ArticaleView(DetailView):
    model=Post
    template_name='blogapp/detail.html'

def logout(request):
    return render(request,"blogapp/logout.html")
    
# def news(request):
   # source = requests.get('https://www.espncricinfo.com/').text
    # soup = BeautifulSoup(source, 'lxml')
    # article = soup.find(class_='img jumbotron-image')
     #return render(request,"blogapp/news.html" ,{'article':article}) 
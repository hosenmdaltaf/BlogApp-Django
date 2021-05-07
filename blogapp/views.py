from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import Post
from .import views
from blogapp.forms import ContactForm
#for email
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import (
     DetailView,
     CreateView,
     ListView,
    #  DeleteView
)
from django.views.generic.edit import(
        DeleteView,
        FormView,
        UpdateView
)
#Homepage view
class HomeView(ListView):
    ordering=['-date']
    paginate_by=6
    template_name='blogapp/blog.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-id')
# post=Post.objects.all().order_by('-id')
# post.view_count =view_count+1
# post.save()


#Detailpage view
class PostDetailView(DetailView):
    model=Post
    template_name='blogapp/detail.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['latest']= Post.objects.order_by('-date')[:5]
        return context

    def get_queryset(self):
         return Post.objects.all()


#post Create page view
class PostCreateView(CreateView):
    model=Post
    fields= ['title','image','details']
    template_name='blogapp/post_create_form.html'
    success_url = reverse_lazy("blogapp:home")

    # def form_valid(self,form):
    #     form.instance.author =self.request.user
    #     return super().form_valid(form)


#post Update page view
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','image','details']
    template_name='blogapp/post_update_form.html'


#post Delete page view
class PostDeleteView(DeleteView):
    model=Post
    template_name='blogapp/delete.html'
    success_url = reverse_lazy("blogapp:home")


#post Contact page view
class Contact_View(FormView):
    template_name = 'blogapp/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("blogapp:home")


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


#post About page view
def about(request):
    return render(request,"blogapp/about.html")


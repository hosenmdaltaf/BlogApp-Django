
from django.urls import path
from .import views
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
from .views import  HomeView,ArticaleView,PostCreateView, PostDeleteView, Contact_View
#from django.conf.urls.static import static
#from django.conf import settings

app_name='blogapp'

urlpatterns = [
    # path('',views.home,name='home'),
    path("",HomeView.as_view(),name='home'),
    path('post/<int:pk>',ArticaleView.as_view(),name='articale-detail'),
    path('post/new',PostCreateView.as_view(),name='post-create'), #PostCreateView.as_view(success_url='/')
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('contact/', Contact_View.as_view(),name='contact'),
    path('about/',views.about,name='about-page')
]

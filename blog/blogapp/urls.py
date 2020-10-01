
from django.urls import path
from .import views
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
from .views import HomeView,ArticaleView
#from django.conf.urls.static import static  
#from django.conf import settings

app_name='blogapp'

urlpatterns = [
    #path('',views.home,name='home'),
    path("",HomeView.as_view(),name='home'),
    #path('news/',views.news,name='news'),
    path('detail/<int:pk>',ArticaleView.as_view(),name='articale-detail'),
    path('',views.logout,name='logout')
]


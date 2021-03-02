
from django.urls import path
from .import views
from .views import(
    HomeView,
    PostDetailView,
    PostCreateView, 
    PostUpdateView,
    PostDeleteView, 
    Contact_View 
    
)  


app_name='blogapp'

urlpatterns = [
    # path('',views.home,name='home'),
    path("",HomeView.as_view(),name='home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='articale-detail'),
    path('post/new',PostCreateView.as_view(),name='post-create'), #PostCreateView.as_view(success_url='/')
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('contact/', Contact_View.as_view(),name='contact'),
    path('about/',views.about,name='about-page')
]

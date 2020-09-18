
from django.urls import path
#from .import views
#from django.contrib.staticfiles.url import staticfiles_urlpatterns
from .views import HomeView
#from django.conf.urls.static import static
#from django.conf import settings

urlpatterns = [
    #path('',views.home),
    path("",HomeView.as_view(),name='home')
]

#if settings.DEBUG:
#urlpatterns += staticfiles_urlpatterns()
    #urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
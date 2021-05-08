
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogapp.urls')),
    path('accounts/',include("accounts.urls")),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     #urlpatterns += staticfiles_urlpatterns()
#     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



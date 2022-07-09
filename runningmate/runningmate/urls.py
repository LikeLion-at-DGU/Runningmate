from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mateapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mateapp.urls')),
    path('mainpage/',include('addproject.urls')),
    path('accounts/',include('allauth.urls')),
    path('login/', views.login, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
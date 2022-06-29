from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = "mateapp"
urlpatterns = [
    path('mainpage',showmain, name = "showmain"),
    path('calendar',calendar, name = "calendar"),
    path('', login, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

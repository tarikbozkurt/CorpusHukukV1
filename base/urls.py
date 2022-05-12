from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from base import views

urlpatterns = [

    path('',views.Base,name='main'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
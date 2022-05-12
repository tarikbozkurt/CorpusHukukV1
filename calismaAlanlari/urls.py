from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from calismaAlanlari import views

urlpatterns = [


    path('calismaAlanlarimiz/',views.calismaAlanlarimiz,name='calismaAlanlarimiz'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from employee import views

urlpatterns = [


    path('ekibimiz/',views.ekip,name='ekibimiz'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
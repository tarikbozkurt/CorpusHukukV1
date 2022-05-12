from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from hakkinda import views
urlpatterns = [


    path('hakkimizda/',views.hakkinda,name='Hakkimizda'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
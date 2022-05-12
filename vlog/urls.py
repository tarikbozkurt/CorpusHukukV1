from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from vlog import views
urlpatterns = [


    path('yayinlar/',views.yayinlar,name='yayinlar'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
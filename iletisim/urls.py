from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from iletisim import views
urlpatterns = [


    path('iletisim/',views.iletisim,name='iletisim'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
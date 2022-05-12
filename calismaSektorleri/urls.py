from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from calismaSektorleri import views

urlpatterns = [


    path('sektorler/', views.calismaSektorler, name='sektorler'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render

# Create your views here.
from base.models import PageSettings
from calismaAlanlari.models import CalismaAlanlari


def calismaAlanlarimiz(request):


    calismaAlanlari = CalismaAlanlari.objects.all()
    page_tag= CalismaAlanlari.objects.all()[:1]
    pageSettings = PageSettings.objects.get(page_title='Çalışma Alanlarımız')
    context={
        'calismaAlanlarimiz':calismaAlanlari,
        'page_tag':page_tag,
        'pageSettings':pageSettings,
    }

    return render(request,'corpushukukv1/hizmetler.html',context)
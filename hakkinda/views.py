from django.shortcuts import render

# Create your views here.
from base.models import PageSettings
from hakkinda.models import Hakkinda,firmaOzellikleri


def hakkinda(request):
    hakkimizda = Hakkinda.objects.all()[2:]
    pageSettings = PageSettings.objects.get(page_title='Hakkımızda')
    firmaOzellik = firmaOzellikleri.objects.all().filter(firmaOzellik_text=str(id))
    context={
        'hakkimizda':hakkimizda,
        'pageSettings':pageSettings,
        'firmaOzellikText':firmaOzellik,


    }
    return render(request,'corpushukukv1/hakkimizda.html',context)

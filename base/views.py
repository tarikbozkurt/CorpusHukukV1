from django.shortcuts import render

# Create your views here.
from base.models import PageSettings
from calismaAlanlari.models import CalismaAlanlari
from employee.models import Employee
from hakkinda.models import Hakkinda, firmaOzellikleri
from vlog.models import Vlog
from calismaSektorleri.models import Sektorler




def AnaSayfa(request):
    anaSayfaHakkimizda = Hakkinda.objects.all()[:2]

    hakkimizda = Hakkinda.objects.all()[:1]
    ekibimiz = Employee.objects.all()
    posts = Vlog.objects.all()[:3]
    calismaAlanlari = CalismaAlanlari.objects.all()

    pageSettings = PageSettings.objects.get(page_tag='ana-sayfa')
    context = {
        'anaSayfaHakkimizda':anaSayfaHakkimizda,
        'hakkimizda': hakkimizda,
        'ekibimiz': ekibimiz,
        'posts': posts,
        'calismaAlanlarimiz': calismaAlanlari,

        'pageSettings': pageSettings,

    }
    return render(request, 'corpushukukv1/anaSayfa.html', context)


def Base(request):
    hakkimizda = Hakkinda.objects.all()[:1]
    hakkimizdaIkinci = Hakkinda.objects.all()[1:]
    ekibimiz = Employee.objects.all()
    posts = Vlog.objects.all()
    footerVlog=Vlog.objects.all()[:5]
    calismaAlanlari = CalismaAlanlari.objects.all()
    sektor = Sektorler.objects.all()
    pageSettings = PageSettings.objects.get(page_tag='ana-sayfa')
    firmaOzellik = firmaOzellikleri.objects.all()
    context = {

        'hakkimizda': hakkimizda,
        'ekibimiz': ekibimiz,
        'posts': posts,
        'sektor' : sektor,
        'hizmetler': calismaAlanlari,
        'firmaOzellik': firmaOzellik,
        'pageSettings': pageSettings,
        'hakkimizdaIkinci':hakkimizdaIkinci,
        'footerVlog':footerVlog,

    }
    return render(request, 'corpushukukv1/base.html', context)

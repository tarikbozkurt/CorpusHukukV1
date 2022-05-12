from django.shortcuts import render

# Create your views here.
import employee
from base.models import PageSettings


def ekip(request):
    ekibimiz = employee.objects.all()
    pageSettings = PageSettings.objects.get(page_title='Ekibimiz')
    context={
        'ekibimiz':ekibimiz,
        'pageSettings':pageSettings,
    }
    return render(request,'corpushukukv1/ekip.html',context)

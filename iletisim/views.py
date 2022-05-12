from django.shortcuts import render

# Create your views here.
from base.models import PageSettings
from iletisim.forms import contactForm
from iletisim.models import firmaBilgi


def iletisim(request):


    pageSettings = PageSettings.objects.get(page_title='İletişim')
    corpusiletisim = firmaBilgi.objects.all()

    form = contactForm(request.POST)

    context = {
        'pageSettings': pageSettings,
        'corpusiletisim': corpusiletisim,
        'form':form,


    }

    return render(request,'corpushukukv1/iletisim.html',context)

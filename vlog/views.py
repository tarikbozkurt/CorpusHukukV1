from django.shortcuts import render

# Create your views here.
from base.models import PageSettings
from vlog.models import Vlog


def yayinlar(request):
    posts = Vlog.objects.all()
    pageSettings = PageSettings.objects.get(page_title='Yayınlarımız')
    context={
        'posts':posts,
        'pageSettings':pageSettings,
    }
    return render(request,'corpushukukv1/vlog.html',context)


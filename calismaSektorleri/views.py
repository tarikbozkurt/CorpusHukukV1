from django.shortcuts import render

# Create your views here.
from calismaSektorleri.models import Sektorler


def calismaSektorler(request):

    calismaSektorleri = Sektorler.objects.all()

from django.shortcuts import render
from django.core import serializers
from .models import Sklad

# Create your views here.

def main(request):
    return render(request, 'main/index.html')


def olish(request):
    return render(request, 'main/olish.html')

def sotish(request):
    sklad = Sklad.objects.all()
    jsonsklad = serializers.serialize('json', sklad)

    # posttovar = ''
    # skladtovar = Sklad.objects.get(tovarnomi=posttovar)

    context = {
        'sklad': sklad,
        'jsklad': jsonsklad

    }

    return render(request, 'main/sotish.html', context)


def skald(request):
    sklad = Sklad.objects.all()
    context = {
        'sklad': sklad,

    }
    return render(request, 'main/sklad.html', context)
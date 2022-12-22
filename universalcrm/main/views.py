from django.shortcuts import render, redirect
from django.core import serializers
from .models import Sklad, Sotish
from .forms import SotishForm

# Create your views here.

def main(request):
    return render(request, 'main/index.html')


def olish(request):
    return render(request, 'main/olish.html')

def sklad(request):
    sklad = Sklad.objects.all()
    jsonsklad = serializers.serialize('json', sklad)
    error = ''
    success1 = ''
    if request.method == 'POST':
        mnomi = request.Post.get('Mahsulotnomi')
        mnarxi = request.Post.get('Mahsulotnarxi')
        smson = request.Post.get('Skalddagimahsulotson')
        x = skald(Mahsulotnomi=mnomi, Mahsulotnarxi=mnarxi, Skalddagimahsulotson=smson )
        x.save()


def sotish(request):
    sklad = Sklad.objects.all()
    jsonsklad = serializers.serialize('json', sklad)

    error = ''
    success = ''
    if request.method == 'POST':
        form = SotishForm(request.POST)

            # if form.is_valid():
        xnomi = request.POST.get('xaridornomi')
        tovarnomi = request.POST.get('tovarnomi')
        tovarnarxi = request.POST.get('tovarnarxi')
        tovarsoni = request.POST.get('tovarsoni')
        jamitovarnarxi = request.POST.get('jamitovarnarxi')
        berilganpul = request.POST.get('berilganpul')
        qarz = request.POST.get('qarz')
        phone = request.POST.get('phone')

        d = Sotish(xaridornomi=xnomi, tovarnomi=tovarnomi, tovarnarxi=tovarnarxi, tovarsoni=tovarsoni,\
                       jamitovarnarxi=jamitovarnarxi, berilganpul=berilganpul,
                       qarz=qarz, phone=phone)
        d.save()
        skladtovar = Sklad.objects.get(tovarnomi=tovarnomi)
        skladtovar.tovarsoni = int(skladtovar.tovarsoni) - int(tovarsoni)
        skladtovar.save()
        success = 'Mahsulot sotildi'
        return redirect('sotish')
        # else:
        #     error = 'Xatolik yuz berdi qayta urinib koring'
    else:
        form = SotishForm()


    # posttovar = ''
    # skladtovar = Sklad.objects.get(tovarnomi=posttovar)

    context = {
        'sklad': sklad,
        'jsklad': jsonsklad,
        'error': error,
        'success': success

    }

    return render(request, 'main/sotish.html', context)


def skald(request):
    sklad = Sklad.objects.all()
    context = {
        'sklad': sklad,

    }
    return render(request, 'main/sklad.html', context)
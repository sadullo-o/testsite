from django.shortcuts import render, redirect
from django.core import serializers
from .models import Sklad, Sotish, Qarz, Qaytarish
from .forms import SotishForm
import math

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
        mnomi = request.POST.get('tovarnomi')
        mnarxi = request.POST.get('tovarnarxi')
        smson = request.POST.get('tovarsoni')

        try:
            skladtovar = Sklad.objects.get(tovarnomi=mnomi)
            skladtovar.tovarsoni = int(skladtovar.tovarsoni) + int(smson)
            skladtovar.tovarnarxi = mnarxi
            skladtovar.save()
            success1 = 'Mahsulot sotildi'
        except:
            x = Sklad(tovarnomi=mnomi, tovarnarxi=mnarxi, tovarsoni=smson)
            x.save()
            success1 = 'Mahsulot sotildi'


        return redirect('sklad')
    return render(request, 'main/sklad.html', {'ss':success1, 'sklad':sklad})


def qaytarish(request):
    qaytarish = Qaytarish.objects.all()
    jsonsklad = serializers.serialize('json', sklad)
    error = ''
    success1 = ''
    if request.method == 'POST':
        xnomi = request.POST.get('xaridornomi')
        tnomi = request.POST.get('tovarnomi')
        tnarx = request.POST.get('tovarnarxi')
        tsoni = request.POST.get('tovarsoni')
        jtnarxi = request.POST.get('jamitovarnarxi')


        try:
            qaytarish = qaytarish.objects.get(xaridornomi=xnomi)
            qaytarish = qaytarish.objects.get(tovarnomi=tnomi)
            qaytarish = qaytarish.objects.get(tovarnarxi=tnarx)
            qaytarish = qaytarish.objects.get(tovarsoni=tsoni)
            qaytarish = qaytarish.objects.get(tovarnomi=jtnarxi)


            qaytarish.skladtovar.jamitovarnarxi = int(qaytarish.tovarsoni) * int(tnarx)
            qaytarish.skladtovar.tovarnarxi = tnarx
            qaytarish.sklad.save()
            success1 = 'Mahsulot sotildi'
        except:
            y = qaytarish(tovarnomi=tnomi, tovarnarxi=tnarx, tovarsoni=tsoni)
            y.save()
            success1 = 'Tovar qaytarildi'


        return redirect('sklad')
    return render(request, 'main/sklad.html', {'ss':success1, 'sklad':sklad})


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

        d = Sotish(xaridornomi=xnomi, tovarnomi=tovarnomi, tovarnarxi=tovarnarxi, tovarsoni=tovarsoni,
                       jamitovarnarxi=jamitovarnarxi, berilganpul=berilganpul,
                       qarz=qarz, phone=phone)
        d.save()
        skladtovar = Sklad.objects.get(tovarnomi=tovarnomi)
        skladtovar.tovarsoni = int(skladtovar.tovarsoni) - int(tovarsoni)
        skladtovar.save()
        try:
            qarzmijoz = Qarz.objects.get(xaridornomi=xnomi)
            qarzmijoz.berganpuli = qarzmijoz.berganpuli + berilganpul
            qarzmijoz.qolganqarzi = qarzmijoz.qolganqarzi + qarz
            qarzmijoz.phone = phone
            qarzmijoz.save()
        except:
            qarzmijoz = Qarz(berganpuli=berilganpul, qolganqarzi=qarz, phone=phone, xaridornomi=xnomi)
            qarzmijoz.save()

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


def qarz(request):
    qarzi = Qarz.objects.all()
    jsonqarz = serializers.serialize('json', qarzi)
    if request.method == 'POST':
        xnomi = request.POST.get('xaridornomi')
        berilganpul = request.POST.get('berganpuli')
        qarz = request.POST.get('qolganqarzi')
        phone = request.POST.get('phone')

        qarzmijoz = Qarz.objects.get(xaridornomi=xnomi)
        qarzmijoz.berganpuli = abs(int(qarzmijoz.berganpuli)) + abs(int(berilganpul))
        qarzmijoz.qolganqarzi = qarz
        qarzmijoz.phone = phone
        qarzmijoz.save()
        return redirect('qarz')

    context = {
        'qarz': jsonqarz,
        'qarzx': qarzi
    }
    return render(request, 'main/qarz.html', context)


#def qaytarish(request):




# crmadmin  --> parol ham login ham
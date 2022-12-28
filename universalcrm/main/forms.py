from .models import Sotish, Sklad, Qaytarish
from django.forms import ModelForm

class SotishForm(ModelForm):
    class Meta:
        model = Sotish
        fields = ['xaridornomi', 'tovarnomi', 'tovarnarxi', 'tovarsoni', 'jamitovarnarxi', 'berilganpul', 'qarz' , 'phone']




class SkladForm(ModelForm):
    class Meta:
        model = Sklad
        fields = ['tovarnomi', 'tovarnarxi', 'tovarsoni']

class QaytarishForm(ModelForm):
    class Meta:
        fields = ['xaridornomi', 'tovarnomi', 'tovarnarxi', 'tovarsoni', 'jamitovarnarxi', 'sana']
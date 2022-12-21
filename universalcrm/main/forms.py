from .models import Sotish
from django.forms import ModelForm

class SotishForm(ModelForm):
    class Meta:
        model = Sotish
        fields = ['xaridornomi', 'tovarnomi', 'tovarnarxi', 'tovarsoni', 'jamitovarnarxi', 'berilganpul', 'qarz' , 'phone']
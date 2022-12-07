from .models import Tovar, Savat
from rest_framework import serializers


class TovarSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Tovar
        fields = ('id', 'title', 'about', 'img', 'narx')



class SavatSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = ('id', 'tovar', 'username', 'phone', 'summa')
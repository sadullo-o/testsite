from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Tovar, Savat
from .serializer import TovarSeralizer, SavatSeralizer

# Create your views here.


class TovarView(ListAPIView):
    queryset = Tovar.objects.all()
    serializer_class = TovarSeralizer



class SavatView(ListCreateAPIView):
    queryset = Savat.objects.all()
    serializer_class = SavatSeralizer
from django.urls import path
from .views import *

urlpatterns = [

    path('', main, name='home'),
    path('olish', olish, name='olish'),
    path('sklad', skald, name='sklad'),
    path('sotish', sotish, name='sotish'),
]
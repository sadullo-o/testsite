from django.urls import path
from .views import *

urlpatterns = [

    path('', main, name='home'),
    path('olish', olish, name='olish'),
    path('sklad', sklad, name='sklad'),
    path('sotish', sotish, name='sotish'),
    path('qarz', qarz, name='qarz'),
    path('qaytarish', qaytarish, name='qaytarish')
]
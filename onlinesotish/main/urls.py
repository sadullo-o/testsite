from django.urls import path

from .views import TovarView, SavatView

urlpatterns = [
    path('tovarlar', TovarView.as_view()),
    path('savat', SavatView.as_view()),
]
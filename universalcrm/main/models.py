from django.db import models
from datetime import datetime
# Create your models here.

class Sklad(models.Model):
    tovarnomi = models.CharField('Tovar nomi', max_length=100)
    tovarnarxi = models.CharField('Tovar narxi', max_length=100)
    tovarsoni = models.CharField('Tovar soni', max_length=100)

    def __str__(self):
        return self.tovarnomi

    class Meta:
        verbose_name = 'Tovar'
        verbose_name_plural = 'Sklad'



class Sotish(models.Model):
    xaridornomi = models.CharField(max_length=200)
    tovarnomi = models.CharField(max_length=200)
    tovarnarxi = models.CharField(max_length=200)
    tovarsoni = models.CharField(max_length=200)
    jamitovarnarxi = models.CharField(max_length=200)
    sotilgansana = models.DateField(default=datetime.now())
    berilganpul = models.CharField(max_length=100)
    qarz = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.xaridornomi

    class Meta:
        verbose_name = 'mahsulot'
        verbose_name_plural = 'Sotilgan mahsulotlar'



class Olish(models.Model):
    firmanomi = models.CharField(max_length=200)
    tovarnomi = models.CharField(max_length=200)
    tovarolishnarxi = models.CharField(max_length=200)
    tovarsotishnarxi = models.CharField(max_length=200)
    tovarsoni = models.CharField(max_length=200)
    jamitovarnarxi = models.CharField(max_length=200)
    olingansana = models.CharField(max_length=100)
    berilganpul = models.CharField(max_length=100)
    qarz = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sana = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.firmanomi

    class Meta:
        verbose_name = 'mahsulot'
        verbose_name_plural = 'Olingan mahsulotlar'


class Qarz(models.Model):
    xaridornomi = models.CharField(max_length=100)
    # tovarnomi = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default='')
    berganpuli = models.CharField(max_length=100)
    qolganqarzi = models.CharField(max_length=100)
    sana = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.xaridornomi


class Qaytarish(models.Model):
    # Mijoz mahsulotni qaytarib bersa
    xaridornomi = models.CharField(max_length=200)
    tovarnomi = models.CharField(max_length=200)
    tovarnarxi = models.CharField(max_length=200)
    tovarsoni = models.CharField(max_length=200)
    jamitovarnarxi = models.CharField(max_length=200)
    beriladiganpul = models.CharField(max_length=200, default='0')
    sana = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.xaridornomi

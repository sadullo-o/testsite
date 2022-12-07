from django.db import models

# Create your models here.

class Tovar(models.Model):
    title =models.CharField(max_length=150)
    about = models.TextField()
    img = models.ImageField()
    narx = models.CharField(max_length=50)


    def __str__(self):
        return self.title


class Savat(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    tovar = models.CharField(max_length=150)
    summa = models.CharField(max_length=50)
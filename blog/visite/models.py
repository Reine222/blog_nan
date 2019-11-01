from django.db import models
from blogger.models import *
from django.contrib.auth.models import User

# Create your models here.
class Visite(models.Model):
    ip = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete =models.CASCADE, related_name='visiteur', null=True)
    pays = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    continent = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    reseau = models.CharField(max_length=50)
    page = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.ip 

class Like(models.Model):
    nombre = models.IntegerField()
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True) 
    article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name="ArticleLike")

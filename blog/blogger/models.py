from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 
from django.dispatch import receiver
# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=50)
    standard = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom



class Article(models.Model):
    titre = models.CharField( max_length=200)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE) 
    categorie = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='article_cat')
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)
    contenu = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    standard = models.BooleanField(default=True)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    nom= models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField()
    sujet = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='images', default='images/user.jpg')
    categorie = models.ForeignKey(Article, on_delete= models.CASCADE)
    standard = models.BooleanField(default=True)

    def __str__(self):
        return self.sujet


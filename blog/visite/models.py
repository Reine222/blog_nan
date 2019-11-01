from django.db import models
from blogger.models import Article
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import HTMLField
from django.utils import timezone




# Create your models here.





# class Category(models.Model):
#     nom = models.CharField(max_length=50)
#     statut = models.BooleanField(default=True)
#     date_add = models.DateTimeField(auto_now_add=True)
#     date_up = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.nom



# class Article(models.Model):
#     titre = models.CharField( max_length=200)
#     user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name='Articleuser_id') 
#     categorie = models.ForeignKey(Category, on_delete= models.CASCADE,related_name='article_cat')
#     image = models.ImageField(upload_to='images')
#     description = models.CharField(max_length=200)
#     content = HTMLField('Content')
#     date= models.DateField(auto_now=False, auto_now_add=True)
#     date_add = models.DateTimeField(auto_now_add=True)
#     date_up = models.DateTimeField(auto_now=True)
#     statut = models.BooleanField(default=True)
#     valider =models.BooleanField()

#     def __str__(self):
#         return self.titre

# class Commentaire(models.Model):
#     nom= models.CharField(max_length=250)
#     email = models.EmailField(max_length=250)
#     date = models.DateTimeField()
#     sujet = models.CharField(max_length=250)
#     message = models.TextField()
#     photo = models.ImageField(upload_to='images', default='images/user.jpg')
#     article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name="ArticleCommentaire")
#     date_add = models.DateTimeField(auto_now_add=True)
#     date_up = models.DateTimeField(auto_now=True)
#     statut = models.BooleanField(default=True)

#     def __str__(self):
#         return self.sujet







class Visite(models.Model):
    ip = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete =models.CASCADE, related_name='UserVisiteur', null=True)
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
    articl = models.ForeignKey(Article, on_delete= models.CASCADE, related_name="ArticleLike")

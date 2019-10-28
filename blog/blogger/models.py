from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import HTMLField

# Create your models here.

class Category(models.Model):
    nom = models.CharField(max_length=50)
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom



class Article(models.Model):
    titre = models.CharField( max_length=200)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE) 
    categorie = models.ForeignKey(Category, on_delete= models.CASCADE,related_name='article_cat')
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)
    content = HTMLField('Content')
    date= models.DateField(auto_now=False, auto_now_add=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    valider =models.BooleanField()

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    nom= models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    date = models.DateTimeField()
    sujet = models.CharField(max_length=250)
    message = models.TextField()
    photo = models.ImageField(upload_to='images', default='images/user.jpg')
    article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name="ArticleCommentaire")
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

    def __str__(self):
        return self.sujet


class Profile(models.Model):

    # Appel de user
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil
    
    # Champs suplementaires
    
    fonction = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    description = models.TextField()
    statut = models.CharField(max_length=50)
    fb_lien =models.URLField(max_length=200)
    tweet_lien =models.URLField(max_length=200)
    ball_lien =models.URLField(max_length=200)
    Be_lien =models.URLField(max_length=200)
    contact =models.CharField(max_length=50)
    valider =models.CharField(max_length=50)
    
    # Initialisation a la creation
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        
        instance.profile.save()





    
    
    
    
def deconnexion(request):
    logout(request)

    return redirect('home') 
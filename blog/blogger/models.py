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
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

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
    standard = models.BooleanField(default=True)

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
    

# Create your models here.
class Header(models.Model):
    logo= models.ImageField(upload_to="images")
    titre=models.CharField(max_length=250)
    image_fond= models.ImageField(upload_to="images")
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    statut= models.BooleanField()


class Footer_one(models.Model):
    titre=models.CharField(max_length=250)
    description= models.TextField()
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    statut= models.BooleanField()


class Footer_two(models.Model):
    titre=models.CharField(max_length=250)
    image_1= models.ImageField(upload_to="images")
    image_2= models.ImageField(upload_to="images")
    image_3= models.ImageField(upload_to="images")
    image_4= models.ImageField(upload_to="images")
    image_5= models.ImageField(upload_to="images")
    image_6= models.ImageField(upload_to="images")
    image_7= models.ImageField(upload_to="images")
    image_8= models.ImageField(upload_to="images")
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    statut= models.BooleanField()

class Footer_trois(models.Model):
    titre=models.CharField(max_length=250)
    description= models.TextField()
    fb_icon= models.URLField(max_length=200)
    tweet_icon= models.URLField(max_length=200)
    ball_icon= models.URLField(max_length=200)
    Be_icon= models.URLField(max_length=200)
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    statut= models.BooleanField()


class Copy(models.Model):
    titre= models.CharField(max_length=250)
    date_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    statut= models.BooleanField()

    # Initialisation a la creation
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        
        instance.profile.save()




    
    
    # image = models.ImageField(upload_to='profile/', default='useravatar.png')
    # fonction= models.CharField(max_length=50)
    # description= models.TextField()
    # fb_icon= models.URLField(max_length=200)
    # tweet_icon= models.URLField(max_length=200)
    # ball_icon= models.URLField(max_length=200)
    # Be_icon= models.URLField(max_length=200)
    # dat_add= models.DateTimeField(auto_now=False, auto_now_add=True)
    # date_upd= models.DateTimeField(auto_now=True, auto_now_add=False)
    # membre=models.BooleanField()
    # visiteur=models.BooleanField()
    
def deconnexion(request):
    logout(request)

    return redirect('home') 
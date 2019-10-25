from django.db import models

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
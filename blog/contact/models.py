from django.db import models

# Create your models here.
class Contact(models.Model):
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    sujet = models.CharField(max_length=50)
    message = models.TextField()
    date_add =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom

class Newsletter(models.Model):
    email = models.EmailField(max_length=50)
    date_add =models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


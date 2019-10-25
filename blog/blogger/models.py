from django.db import models

# Create your models here.
class Model_Date(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(Model_Date):
    nom = models.CharField( max_length=50)
    image = models.ImageField(upload_to='images')
    user = models.CharField(max_length=50) 
    statut = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Tag(Model_Date):
    nom = models.CharField( max_length=50)
    statut = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom

class Article(Model_Date):
    titre = models.CharField( max_length=200)
    autheur = models.CharField(max_length=50)
    categorie = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='article_cat')
    tag = models.ManyToManyField(Tag, on_delete= models.CASCADE, related_name='article_tag')
    image = models.ImageField(upload_to='images')
    contenu = models.TextField()
    statut = models.BooleanField(default=True)

    def __str__(self):
        return self.titre

class Commentaire(Model_Date):
    user_name= models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    sujet = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    categorie = models.ForeignKey(Article, on_delete= models.CASCADE)
    statut = models.BooleanField(default=True)

    def __str__(self):
        return self.sujet


# from django.db import models
# from blogger.models import Article
# from django.contrib.auth.models import User

# # Create your models
# class Visiteur(models.Model):
#     username = models.CharField(max_length=50)
#     #adresse_ip = models.IPAddressField()


# class Client(models.Model):
#     ip = models.GenericIPAddressField()
#     # username = models.CharField(max_length=50)
#     pays = models.CharField(max_length=50)
#     ville = models.CharField(max_length=50)
#     continent = models.CharField(max_length=50)
#     longitude = models.FloatField()
#     latitude = models.FloatField()
#     reseau = models.CharField(max_length=50)
#     page = models.CharField(max_length=200,null=True)
#     def __str__(self):
#         return self.ip 

# class Like(models.Model):
#     nombre = models.IntegerField()
#     user = models.ForeignKey(User, on_delete= models.CASCADE) 
#     article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name="ArticleLike")




# from django import forms
# from blogger.models import Article
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from tinymce import HTMLField


# class Post(forms.Form):
#     titre = forms.CharField(label='titre', max_length=200)
#     user_id = forms.CharField(label='Username', max_length=200, required=False)
#     categorie = forms.CharField(label='Categorie', max_length=200, required=False)
#     image = forms.ImageField(label='Image')
#     description = forms.CharField(label='Description', max_length=200)
#     content = HTMLField('Content', label='Description')
#     date= forms.DateField(auto_now=False, auto_now_add=True)
#     date_add = forms.DateTimeField(auto_now_add=True)
#     date_up = forms.DateTimeField(auto_now=True)
#     statut = forms.BooleanField(default=True)
#     valider =forms.BooleanField()

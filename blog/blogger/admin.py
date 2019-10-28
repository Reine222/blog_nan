# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'statut', 'date_add', 'date_up')
    list_filter = (
        'statut',
        'date_add',
        'date_up',
        'id',
        'nom',
        'statut',
        'date_add',
        'date_up',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'user_id',
        'categorie',
        'image',
        'description',
        'content',
        'date',
        'date_add',
        'date_up',
        'statut',
        'valider',
    )
    list_filter = (
        'user_id',
        'categorie',
        'date',
        'date_add',
        'date_up',
        'statut',
        'valider',
        'id',
        'titre',
        'user_id',
        'categorie',
        'image',
        'description',
        'content',
        'date',
        'date_add',
        'date_up',
        'statut',
        'valider',
    )


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'email',
        'date',
        'sujet',
        'message',
        'photo',
        'article',
        'date_add',
        'date_up',
        'statut',
    )
    list_filter = (
        'date',
        'article',
        'date_add',
        'date_up',
        'statut',
        'id',
        'nom',
        'email',
        'date',
        'sujet',
        'message',
        'photo',
        'article',
        'date_add',
        'date_up',
        'statut',
    )


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'fonction',
        'image',
        'description',
        'statut',
        'fb_lien',
        'tweet_lien',
        'ball_lien',
        'Be_lien',
        'contact',
        'valider',
    )
    list_filter = (
        'user',
        'valider',
        'id',
        'user',
        'fonction',
        'image',
        'description',
        'statut',
        'fb_lien',
        'tweet_lien',
        'ball_lien',
        'Be_lien',
        'contact',
        'valider',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Profile, ProfileAdmin)

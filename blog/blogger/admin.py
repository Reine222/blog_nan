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
        'contenu',
        'date_add',
        'date_up',
        'statut',
    )
    list_filter = (
        'user_id',
        'categorie',
        'date_add',
        'date_up',
        'statut',
        'id',
        'titre',
        'user_id',
        'categorie',
        'image',
        'description',
        'contenu',
        'date_add',
        'date_up',
        'statut',
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
        'standard',
    )
    list_filter = (
        'date',
        'article',
        'standard',
        'id',
        'nom',
        'email',
        'date',
        'sujet',
        'message',
        'photo',
        'article',
        'standard',
    )


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'fonction',
        'image',
        'description',
        'statut',
    )
    list_filter = (
        'user',
        'id',
        'user',
        'fonction',
        'image',
        'description',
        'statut',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Profile, ProfileAdmin)

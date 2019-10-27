from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class HeaderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'logo',
        'titre',
        'image_fond',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'logo',
        'titre',
        'image_fond',
        'date_add',
        'date_upd',
        'statut',
    )


class Footer_oneAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
    )


class Footer_twoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'image_1',
        'image_2',
        'image_3',
        'image_4',
        'image_5',
        'image_6',
        'image_7',
        'image_8',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'image_1',
        'image_2',
        'image_3',
        'image_4',
        'image_5',
        'image_6',
        'image_7',
        'image_8',
        'date_add',
        'date_upd',
        'statut',
    )


class Footer_troisAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'fb_icon',
        'tweet_icon',
        'ball_icon',
        'Be_icon',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'description',
        'fb_icon',
        'tweet_icon',
        'ball_icon',
        'Be_icon',
        'date_add',
        'date_upd',
        'statut',
    )


class CopyAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'date_add', 'date_upd', 'statut')
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'date_add',
        'date_upd',
        'statut',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Header, HeaderAdmin)
_register(models.Footer_one, Footer_oneAdmin)
_register(models.Footer_two, Footer_twoAdmin)
_register(models.Footer_trois, Footer_troisAdmin)
_register(models.Copy, CopyAdmin)

from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'email', 'sujet', 'message', 'date_add')
    list_filter = (
        'date_add',
        'id',
        'nom',
        'email',
        'sujet',
        'message',
        'date_add',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'date_add', 'date_up')
    list_filter = (
        'date_add',
        'date_up',
        'id',
        'email',
        'date_add',
        'date_up',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)
_register(models.Newsletter, NewsletterAdmin)

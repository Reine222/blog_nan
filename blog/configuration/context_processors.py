from .models import *

def config(request):
    header  = Header.objects.filter(statut=True)[:5]
    footer_one = Footer_one.objects.filter(statut=True)[:1]
    footer_one1 = Footer_one.objects.filter(statut=True)[1:]
    footer_two = Footer_two.objects.filter(statut=True)[:1]
    footer_trois = Footer_trois.objects.filter(statut=True)[:1]
    copy = Copy.objects.filter(statut=True)[:1]

    data = {
        'header':header,
        'footer_one': footer_one,
        'footer_one1': footer_one1,
        'footer_two': footer_two,
        'footer_trois': footer_trois,
        'copy': copy,
    }

    return data

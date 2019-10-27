from .models import *

def config(request):
    header  = Header.objects.filter(statut=True)[:1]
    header1  = Header.objects.filter(statut=True)[1:2]
    header2  = Header.objects.filter(statut=True)[2:3]
    header3  = Header.objects.filter(statut=True)[3:4]
    header4  = Header.objects.filter(statut=True)[4:5]
    header5  = Header.objects.filter(statut=True)[5:]
    footer_one = Footer_one.objects.filter(statut=True)[:1]
    footer_one1 = Footer_one.objects.filter(statut=True)[1:]
    footer_two = Footer_two.objects.filter(statut=True)[:1]
    footer_trois = Footer_trois.objects.filter(statut=True)[:1]
    copy = Copy.objects.filter(statut=True)[:1]

    data = {
        'header':header,
        'header1':header1,
        'header2':header2,
        'header3':header3,
        'header4':header4,
        'header5':header5,
        'footer_one': footer_one,
        'footer_one1': footer_one1,
        'footer_two': footer_two,
        'footer_trois': footer_trois,
        'copy': copy,
    }

    return data

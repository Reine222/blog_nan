from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Contact, Newsletter

# Create your views here.

def contact(request):
    return render(request, 'pages/contact.html')

def senddata(request):
    postdata = json.loads(request.body.decode('utf-8'))
    name = postdata['name']
    email = postdata['email']
    subject = postdata['suject']
    message = postdata['message']
    succes = False
    try:
        contact = Contact()
        contact.nom = name
        contact.email = email
        contact.sujet = subject
        contact.message = message
        contact.save()
        succes = True
        reponse = 'Votre message a bien été envoyé, nous vous remercions de nous avoir contacté !'
    except:
        succes = False
        reponse = "Un probleme survennu lors de l'enregistrement"

    datas = {
        'succes':succes,
        'reponse':reponse,
    }
    
    return JsonResponse(datas, safe=False)


def letter(request):
    postdata = json.loads(request.body.decode('utf-8'))
    email = postdata['email']
    succes = False
    try:
        newsletter = Newsletter()
        newsletter.email = email
        newsletter.save()
        succes = True
        reponse = 'Vous avez été bien enregistré!'
    except:
        succes = False
        reponse = "Probleme d'enregistrement !"

    datas = {
        'succes':succes,
        'reponse':reponse,
    }
    
    return JsonResponse(datas, safe=False)
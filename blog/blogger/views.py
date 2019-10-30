from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from twilio.rest import Client
from django.http import JsonResponse
import json
from datetime import datetime, timedelta, timezone, tzinfo
import requests
import uuid 

# Create your views here.
def home(request):
    
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    articlee= Article.objects.filter(statut=True)[1:]

    if request.POST :
        recherche = request.POST.get('search2')
        pag_Articles =Article.objects.all().filter(titre__icontains= recherche).order_by('titre')
        
    else:
        pag_Articles = Article.objects.all().order_by('-id')
        
    try:
        paginator = Paginator(pag_Articles, 3)
        page = request.GET.get('page')
        pag_Article = paginator.get_page(page)
    except EmptyPage:
        pag_Article = paginator(1)
    except   PageNotAnInteger:
        pag_Article = paginator(paginator.num_pages)

    #firstcat = Category.objects.filter(statut=True)[:1]
    # for item in firstcat:
    #     first= item
    #     act_articles= first.article_cat.all()
    


    data ={
        'categories': categories,
        'articles': pop_articles,
        #'act_articles': act_articles,
        'article': article,
        'articlee': articlee,
        'pag_Article': pag_Article,
        
    }

    return render(request, 'pages/index.html', data)

def selectCat(request, id):
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)

    selectcat_arts = Article.objects.filter(categorie__pk = id ).order_by('-id')
        
    try:
        paginator = Paginator(selectcat_arts, 3)
        page = request.GET.get('page')
        pag_Article = paginator.get_page(page)
    except EmptyPage:
        pag_Article = paginator(1)
    except PageNotAnInteger:
        pag_Article = paginator(paginator.num_pages)

    data ={
        'categories': categories,
        'articles': pop_articles,
        'act_articles': selectcat_arts,
        'pag_Article':pag_Article,
    }
    return render(request, 'pages/index.html', data )


def category(request):
    
    catego = Category.objects.filter(statut=True)
    articles = Article.objects.filter(statut=True)
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)

    if request.POST :
        recherche = request.POST.get('searchcat')
        pag_Articles = article.filter(titre__icontains= recherche).order_by('titre')
       
    else:
        pag_Articles = article.order_by('-id')
        
    try:
        paginator = Paginator(pag_Articles, 4)
        page = request.GET.get('page')
        pag_Article = paginator.get_page(page)
    except EmptyPage:
        pag_Article = paginator(1)
    except   PageNotAnInteger:
        pag_Article = paginator(paginator.num_pages)
    
    data= {
        'catego': catego,
        'articles': articles,
        'articles': pop_articles,
        'categories': categories,
        'article': article,
        'pag_Article':pag_Article,
    }
    return render(request, 'pages/category.html', data )

def archive(request):
    catego = Category.objects.filter(statut=True)
    articles = Article.objects.filter(statut=True)
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    
    if request.POST :
        recherche = request.POST.get('searcharchive')
        pag_Articles = article.filter(titre__icontains= recherche).order_by('titre')
       
    else:
        pag_Articles = article.order_by('-id')
        
    try:
        paginator = Paginator(pag_Articles, 4)
        page = request.GET.get('page')
        pag_Article = paginator.get_page(page)
    except EmptyPage:
        pag_Article = paginator(1)
    except   PageNotAnInteger:
        pag_Article = paginator(paginator.num_pages)

    data= {
        'catego': catego,
        'articles': articles,
        'articles': pop_articles,
        'categories': categories,
        'article': article,
        'pag_Article':pag_Article,
    }
    return render(request, 'pages/archive.html', data)


def single(request, pk):
    arts = Article.objects.get(pk=pk)
   
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    commentaires = Commentaire.objects.filter(article__pk = pk ).order_by('-id')
    article_id = pk
    #user articles
    #user = arts.user_id.id
    #user_articles = Article.objects.filter(user_id__id=user).order_by('pk')
    all_arts = Article.objects.filter(statut=True).exclude(pk=article_id).order_by('pk')
    #print(user_articles)
    try:
        paginator = Paginator(all_arts, 2)
        page = request.GET.get('page')
        pag_Article = paginator.get_page(page)
        print('pag_Article = ', pag_Article )
    except EmptyPage:
        pag_Article = paginator(1)
    except PageNotAnInteger:
        pag_Article = paginator(paginator.num_pages)

    data ={
        'arts': arts,
        'articles': pop_articles,
        'categories': categories,
        'article': article,
        'commentaires': commentaires,
        'article_id':article_id,
        #'user_articles':user_articles,
        'pag_Article': pag_Article,
        
    }

    return render(request, 'pages/single.html', data)


########################### def generate  code ###########################

def codes():
    id = uuid.uuid4() 
    return id
    print (id)


########################## def twilio ######################################










########################## def email ######################################



def envoiEmail(requests):
    url= 'http://mysiteapi.tk/html'
    
    data = {
        'subject': "Demande d'un compte membre" ,
        'message': "<p><b> Veiller valider sa Demande </b></p>" ,
        'to': "koulaireine0222@gmail.com" ,
        'key': ")H@MbQeThWmZq4t7w!z%C*F-JaNdRgUj" ,
    }
    req = requests.post(url, data=data)
    return req.text
    print(req.text)


def envoimail(requests):
    url= 'http://mysiteapi.tk/html'
    
    data = {
            'subject': "Code de validation" ,
            'message': "<p><i> Voici votre code de validation :</i> <b>BlogNan2019*</b></p>" ,
            'to': "koulaireine0222@gmail.com" ,
            'key': ")H@MbQeThWmZq4t7w!z%C*F-JaNdRgUj" ,
        }
    req = requests.post(url, data=data)
        # return req.text
    print(req.text)





def register(request):
    if request.method == "POST":
        nom=request.POST.get('nom')   
        prenom=request.POST.get('prenom')   
        fonction=request.POST.get('fonction')
        description = request.POST.get('description')
        
        fb_lien=request.POST.get('fb_lien')
        statut=request.POST.get('statut')
        tweet_lien=request.POST.get('tweet_lien')
        ball_lien=request.POST.get('ball_lien')
        Be_lien=request.POST.get('Be_lien')
        contact=request.POST.get('contact')
        # valider=request.POST.get('valider')
        
        image=request.FILES.get('image')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('pass')
        repeat_pass=request.POST.get('repeat-pass')
        print('\r\n',nom,prenom,fonction,description,statut,image,email,contact,username,fb_lien,tweet_lien,ball_lien,Be_lien,password,repeat_pass,'\r\n')
        if password == repeat_pass:
            user = User(
                username=username,
                first_name=nom,
                last_name=prenom,
                email=email,
                
            )
            try:
                user.save()
                user.profile.description=description
                user.profile.statut=statut
                user.profile.fonction=fonction
                user.profile.contact=contact
                user.profile.fb_lien=fb_lien
                user.profile.tweet_lien=tweet_lien
                user.profile.ball_lien=ball_lien
                user.profile.Be_lien=Be_lien
                user.profile.image=image
                
                
                
                
                user.profile.save()
                user.password = password
                user.set_password(user.password)
                user.save()
                
                #prof = Profile(nom=nom,prenom=prenom,description=description,statut=statut,image=image,email=email,contact=contact,username=username,fb_lien=fb_lien,tweet_lien=tweet_lien,ball_lien=ball_lien,Be_lien=Be_lien)
                #prof.user.save()
                
                print('success')
                url= 'http://mysiteapi.tk/html'
    
                data = {
                    'subject': "Demande d'un compte membre: 21596@hk",
                    'message': "<p><b> Voici botre code : </b>Code</p>" ,
                    'to': "koulaireine0222@gmail.com" ,
                    'key': ")H@MbQeThWmZq4t7w!z%C*F-JaNdRgUj" ,
                }
                req = requests.post(url, data=data)
                # return req.text
                print(req.text)
                
                return redirect('confirmer')
                
          
                
                
            except:
                print('error')
                

    return render(request,'pages/register.html')

def connect(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        _next = request.GET.get('next', False)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            
            
            print("user is login")

            login(request, user)
            if _next: 
                return redirect(_next)
            else:
                return redirect('home')
        else:
            return render(request, 'pages/connexion.html')
    return render(request, 'pages/connexion.html')

def deconection(request):
    logout(request)
    return redirect('connect')

def confirm(request):
    postdata = json.loads(request.body.decode('utf-8'))
    code = "21596@hk"
    confirme = postdata['confirme']
    message = ''
    issuccess= False
    if confirme == code :
        issuccess= True
        
        ## Email def
        url= 'http://mysiteapi.tk/html'
    
        data = {
            'subject': "Demande d'un compte membre" ,
            'message': "<p><b> Veiller valider sa Demande </b></p>" ,
            'to': "koulaireine0222@gmail.com" ,
            'key': ")H@MbQeThWmZq4t7w!z%C*F-JaNdRgUj" ,
        }
        req = requests.post(url, data=data)
        # return req.text
        print(req.text)
        
        
        
        url= 'http://mysiteapi.tk/html'
    
        data = {
            'subject': "Demande d'un compte membre" ,
            'message': "<p><b> V </b></p>" ,
            'to': "koulaireine0222@gmail.com" ,
            'key': ")H@MbQeThWmZq4t7w!z%C*F-JaNdRgUj" ,
        }
        req = requests.post(url, data=data)
        # return req.text
        print(req.text)
        
        
        
        
        message = 'Votre inscription a été effectuée , veuillez verifier votre boite de messagereie, vous recevrez le lien de connexion par mail !'
        # resultat= Confirmer(confirme = confirme)
        # resultat.save()
        print(confirme)

        
    else:
        issuccess= False
        message = 'Code incorrecte, veuillez verifier votre code'
    
    datas = {
        
        'issuccess':issuccess,
        'confirme':confirme,
        'message': message,
    }
    return JsonResponse(datas, safe=False)


def confirmer(request):
    return render(request, 'pages/confirmation.html')

def comment(request):
    postdata = json.loads(request.body.decode('utf-8'))
    name = postdata['name']
    email = postdata['email']
    subject = postdata['suject']
    message = postdata['message']
    article_id = postdata['article_id']
    article = Article.objects.get(pk= article_id)
    succes = False
    try:
        commentaire = Commentaire()
        commentaire.nom = name
        commentaire.email = email
        commentaire.date = datetime.now()
        commentaire.sujet = subject
        commentaire.message = message
        commentaire.article = article
        commentaire.save()
        succes = True
        reponse = 'Votre commentaire a bien été enregisté '
    except:
        succes = False
        reponse = "Un probleme survennu lors de l'enregistrement"

    datas = {
        'succes':succes,
        'reponse':reponse,
    }
    
    return JsonResponse(datas, safe=False)



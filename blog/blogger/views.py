from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from twilio.rest import Client
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)
    firstcat = Category.objects.filter(statut=True)[:1]
    article= Article.objects.filter(statut=True)
    articlee= Article.objects.filter(statut=True)[1:]
    
    
    for item in firstcat:
        first= item
    act_articles = first.article_cat.all

    
    # try:
    #     paginator = Paginator(act_articles, 1)
    #     page = request.GET.get('page', 1)
    #     cat_articles = paginator.get_page(page)
    # except EmptyPage:
    #     cat_articles = paginator(1)
    # except PageNotAnInteger:
    #     cat_articles = paginator(paginator.num_pages)
    
    


    data ={
        'categories': categories,
        'articles': pop_articles,
        'act_articles': act_articles,
        'article': article,
        'articlee': articlee,
        
    }

    return render(request, 'pages/index.html', data)

def selectCat(request, id):
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)
    selectcat_arts = Article.objects.filter(categorie__pk = id )
    print('selectcat_arts=', selectcat_arts)

    data ={
        'categories': categories,
        'articles': pop_articles,
        'act_articles': selectcat_arts,
    }
    return render(request, 'pages/index.html', data )


def category(request):
    
    catego = Category.objects.filter(statut=True)
    articles = Article.objects.filter(statut=True)
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    
    data= {
        'catego': catego,
        'articles': articles,
        'articles': pop_articles,
        'categories': categories,
        'article': article,
    }
    return render(request, 'pages/category.html', data )





def archive(request):
    return render(request, 'pages/archive.html')




def single(request, pk):
    arts = Article.objects.get(pk=pk)
    pop_articles = Article.objects.filter(statut=True)[:4]
    categories = Category.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    
    

    data ={
        'arts': arts,
        'articles': pop_articles,
        'categories': categories,
        'article': article,
        
    }

    return render(request, 'pages/single.html', data)

# def genere():
#     code='BlogNan2019*'
#     account_sid = 'ACcd70283e1ee00056836d33ddb10ceb53'
#     auth_token = 'b3169a7d3ed1082856a8dd7c5f9f3432'
#     client = Client(account_sid, auth_token)

#     message = client.messages \
#         .create(
#             body='Votre Code de validation est le suivant: {}'.format(code),
#             from_='+18049772449',
#             to='+22553858586'
#         )
#     return(message.sid)


def register(request):
    if request.method == "POST":
        nom=request.POST.get('nom')   
        prenom=request.POST.get('prenom')   
        fonction=request.POST.get('fonction')
        description=request.POST.get('description')
        membre=request.POST.get('membre')
        fb_lien=request.POST.get('fb_lien')
        tweet_lien=request.POST.get('tweet_lien')
        ball_lien=request.POST.get('ball_lien')
        Be_lien=request.POST.get('Be_lien')
        contact=request.POST.get('contact')
        
        image=request.FILES.get('image')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('pass')
        repeat_pass=request.POST.get('repeat-pass')
        print('\r\n',nom,prenom,fonction,description,membre,image,email,username,fb_lien,tweet_lien,ball_lien,Be_lien,contact,password,repeat_pass,'\r\n')
        if password == repeat_pass:
            user = User(
                username=username,
                first_name=nom,
                last_name=prenom,
                email=email
            )
            try:
                user.save()
                user.profile.fonction=fonction
                user.profile.image=image
                user.profile.desciption=description
                user.profile.membre=membre
                
                user.save()
                user.password = password
                user.set_password=user.password
                user.save()
                print('success')
                genere()
                return redirect('confirmer')
            except:
                print('error')
                # return redirect('inscription')

    return render(request,'pages/register.html')

def connect(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        _next = request.GET.get('next', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            
            print("user is login")

            login(request, user)
            if _next: 
                return redirect(_next)
            else:
                return redirect('dashboard')
        else:
            return render(request, 'pages/connexion.html')
    return render(request, 'pages/connexion.html')
@login_required(login_url='connection')

def deconection(request):
    logout(request)
    return redirect('connect')

def confirm(request):
    postdata = json.loads(request.body.decode('utf-8'))
    #name = postdata['name']
    confirme = postdata['confirme']
    message = ''
    issuccess= False
    code= 'BlogNan2019*'
    if confirme == code :
        issuccess= True
        message = 'Merci pour votre inscription, votre compte est en cours de validation'
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
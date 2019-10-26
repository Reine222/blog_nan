from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home(request):
    categories = Category.objects.filter(statut=True)
    pop_articles = Article.objects.filter(statut=True)[:4]
    #firstcat = Category.objects.filter(statut=True)[:1]
    #articles = Article.objects.filter(statut=True)

    #articles = firstcat.article_cat.all() 
    #print(firstcat)

    data ={
        'categories': categories,
        'articles': pop_articles,
    }

    return render(request, 'pages/index.html', data)

def category(request):
    return render(request, 'pages/category.html')

def element(request):
    return render(request, 'pages/element.html')

def archive(request):
    return render(request, 'pages/archive.html')

def single(request):
    return render(request, 'pages/single.html')

def register(request):
    if request.method == "POST":
        nom=request.POST.get('nom')   
        prenom=request.POST.get('prenom')   
        fonction=request.POST.get('fonction')
        description=request.POST.get('description')
        membre=request.POST.get('membre')
        
        image=request.FILES.get('image')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('pass')
        repeat_pass=request.POST.get('repeat-pass')
        print('\r\n',nom,prenom,fonction,description,membre,image,email,username,password,repeat_pass,'\r\n')
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


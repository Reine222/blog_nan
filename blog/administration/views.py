from django.shortcuts import render
from blogger.models import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.








def index_dash(request):
    # catego= Article.objects.filter(categorie__pk = pk ).order_by('-id')
    # categorie__id = pk
    profil= Profile.objects.all()[:1]
    comment= Commentaire.objects.filter(statut=True, article__valider=True)
    catego= Category.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    articl= Article.objects.filter(statut=True, valider=True )
    articles= Article.objects.filter(statut=True, valider=True )
    articlee= Article.objects.filter(statut=True, valider=False )
    context = {"catego": catego, "comment": comment, "profil": profil, "article": article, "articles": articles, "articlee": articlee,}
    
    return render(request, 'pages/index_dash.html', context)

def admin_visiteur_dash(request):
    article = Article.objects.filter(statut=True, valider=True)
    commentaires = Commentaire.objects.filter(statut=True, article__valider=True)
    data = {
        'commentaire': commentaires,
        'article':article,
    }
    return render(request, 'pages/admin_visiteur_dash.html', data)

def detail_visiteur_dash(request, id):
    selectarticle = Article.objects.get(pk=id)
    commentaire = Commentaire.objects.filter(article__id = id, article__valider=True)
    profil= Profile.objects.all()[:1]
    context = {
        "profil": profil,
        'selectarticle':selectarticle,
        'commentaire':commentaire,
        }
    return render(request, 'pages/detaill_visiteur_dash.html', context)

def page_dash(request):
    return render(request, 'pages/page_dash.html')

def post_attend_dash(request):
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True, article__valider=True)
    articlee= Article.objects.filter(statut=True, valider=False )
    context = {"articlee": articlee, "commente": commente, "profil": profil,}
    return render(request, 'pages/post_attend_dash.html', context)

def post_partage_dash(request):
    profil= Profile.objects.all()[:1]
    context = {"profil": profil,}
    return render(request, 'pages/post_partage_dash.html', context)

def post_valid_dash(request):
    profil= Profile.objects.all()[:1]
    
    articles= Article.objects.filter(statut=True, valider=True )
    context = {"articles": articles, "profil": profil,}
    
    return render(request, 'pages/post_valid_dash.html', context)

def profil_visiteur_dash(request):
    return render(request, 'pages/profil_visiteur_dash.html')

def form_article_dash(request):
    message = ''
    catego= Category.objects.filter(statut=True)
    prof= Profile.objects.all()
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True, article__valider=True)
    context = {"commente": commente, "profil": profil,"prof": prof,"catego": catego}
    
    if request.method == "POST":
        titre = request.POST.get('titre')
        user_id = request.POST.get('username')
        user = User.objects.get(pk=5)
        categorie_id = request.POST.get('categorie')
        categorie = Category.objects.get(pk=2)
        image = request.FILES.get('image')
        description = request.POST.get('description')
        content = request.POST.get('content')
        #print("Titre=",titre,"userid=",user_id,"categori_id=",categorie_id,"image=",image,'description=',description,'content=',content)
        print('user=',user)
        print('categorie=', categorie)
        
        article = Article()
        article.titre = titre
        article.user_id = user
        article.categorie = categorie
        article.image = image
        article.description = description
        article.valider = False
        article.content = content
        article.save()
        #message="Article enregistré avec succes !"
        
        #message="Probleme d'enregistrement!"
        #print('error enregistrement')

    context = {
        "commente": commente, 
        "profil": profil,
        "prof": prof,
        "catego": catego,
        'message':message,
    }


    return render(request, 'pages/form_article_dash.html', context)

def form_profil_dash(request):
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True, article__valider=True)
    context = {"commente": commente,"profil": profil, "profil": profil,}
    return render(request, 'pages/form_profil_dash.html', context)

def project_detail_dash(request, pk):
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True, article__valider=True)
    article= Article.objects.filter(statut=True)
    art = Article.objects.get(pk=pk)
    comment = Commentaire.objects.filter(article__valider = True, article__pk = pk).order_by('-id')
    context = {"article": article,"profil": profil, "commente": commente, "art": art, "comment": comment,}
    return render(request, 'pages/project_detail_dash.html', context)

def tables_dash(request):
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True, article__valider=True)
    article= Article.objects.filter(statut=True)
    context = {"article": article, "commente": commente,"profil": profil,}
    return render(request, 'pages/tables_dash.html', context)

def tables_visiteur_dash(request):
    article= Article.objects.filter(statut=True)
    data = {
        'article':article,
    }
    return render(request, 'pages/tables_visiteur_dash.html', data)



def ip_adrress(request):
    return render(request, 'bases/base.html', context=RequestContext(request))



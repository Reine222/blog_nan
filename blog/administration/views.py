from django.shortcuts import render
from blogger.models import *

# Create your views here.

def index_dash(request):
    # catego= Article.objects.filter(categorie__pk = pk ).order_by('-id')
    # categorie__id = pk
    profil= Profile.objects.all()[:1]
    comment= Commentaire.objects.filter(statut=True)
    catego= Category.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    articles= Article.objects.filter(statut=True, valider=True )
    articlee= Article.objects.filter(statut=True, valider=False )
    context = {"catego": catego, "comment": comment, "profil": profil, "article": article, "articles": articles, "articlee": articlee,}
    
    return render(request, 'pages/index_dash.html', context)

def admin_visiteur_dash(request):
    commentaires = Commentaire.objects.filter(statut=True)
    data = {
        'commentaire': commentaires,
    }
    return render(request, 'pages/admin_visiteur_dash.html', data)

def detail_visiteur_dash(request):
    profil= Profile.objects.all()[:1]
    context = {"profil": profil,}
    return render(request, 'pages/detaill_visiteur_dash.html', context)

def page_dash(request):
    return render(request, 'pages/page_dash.html')

def post_attend_dash(request):
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True)
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
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True)
    context = {"commente": commente, "profil": profil,}
    return render(request, 'pages/form_article_dash.html', context)

def form_profil_dash(request):
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True)
    context = {"commente": commente,"profil": profil, "profil": profil,}
    return render(request, 'pages/form_profil_dash.html', context)

def project_detail_dash(request, pk):
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    art = Article.objects.get(pk=pk)
    comment = Commentaire.objects.filter(article__pk = pk ).order_by('-id')
    context = {"article": article,"profil": profil, "commente": commente, "art": art, "comment": comment,}
    return render(request, 'pages/project_detail_dash.html', context)

def tables_dash(request):
    profil= Profile.objects.all()[:1]
    commente= Commentaire.objects.filter(statut=True)
    article= Article.objects.filter(statut=True)
    context = {"article": article, "commente": commente,"profil": profil,}
    return render(request, 'pages/tables_dash.html', context)

def tables_visiteur_dash(request):
    return render(request, 'pages/tables_visiteur_dash.html')





def ip_adrress(request):
    return render(request, 'pages/index.html', context=RequestContext(request))



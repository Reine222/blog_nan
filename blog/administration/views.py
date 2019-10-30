from django.shortcuts import render
from blogger.models import *

# Create your views here.

def index_dash(request):
    article= Article.objects.filter(statut=True, )
    context = {"article": article,}
    
    return render(request, 'pages/index_dash.html', context)

def admin_visiteur_dash(request):
    return render(request, 'pages/admin_visiteur_dash.html')

def detail_visiteur_dash(request):
    return render(request, 'pages/detaill_visiteur_dash.html')

def page_dash(request):
    return render(request, 'pages/page_dash.html')

def post_attend_dash(request):
    return render(request, 'pages/post_attend_dash.html')

def post_partage_dash(request):
    return render(request, 'pages/post_partage_dash.html')

def post_valid_dash(request):
    return render(request, 'pages/post_valid_dash.html')

def profil_visiteur_dash(request):
    return render(request, 'pages/profil_visiteur_dash.html')

def form_article_dash(request):
    return render(request, 'pages/form_article_dash.html')

def form_profil_dash(request):
    return render(request, 'pages/form_profil_dash.html')

def project_detail_dash(request, pk):
    article= Article.objects.filter(statut=True)
    art = Article.objects.get(pk=pk)
    comment = Commentaire.objects.filter(article__pk = pk ).order_by('-id')
    context = {"article": article, "art": art, "comment": comment,}
    return render(request, 'pages/project_detail_dash.html', context)

def tables_dash(request):
    article= Article.objects.filter(statut=True)
    context = {"article": article,}
    return render(request, 'pages/tables_dash.html', context)

def tables_visiteur_dash(request):
    return render(request, 'pages/tables_visiteur_dash.html')
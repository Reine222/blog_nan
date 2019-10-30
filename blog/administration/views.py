from django.shortcuts import render

# Create your views here.

def index_dash(request):
    return render(request, 'pages/index_dash.html')

def admin_visiteur_dash(request):
    return render(request, 'pages/admin_visiteur_dash.html')

def detail_visiteur_dash(request):
    return render(request, 'pages/detail_visiteur_dash.html')

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

def form_aricle_dash(request):
    return render(request, 'pages/form_aricle_dash.html')

def form_profil_dash(request):
    return render(request, 'pages/form_profil_dash.html')

def project_detail_dash(request):
    return render(request, 'pages/project_detail_dash.html')

def tables_dash(request):
    return render(request, 'pages/tables_dash.html')

def tables_visiteur_dash(request):
    return render(request, 'pages/tables_visiteur_dash.html')
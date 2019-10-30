from django.shortcuts import render

# Create your views here.

def index_dash(request):
    return render(request, 'pages/index_dash.html')

def page_dash(request):
    return render(request, 'pages/page_dash.html')

def post_attend_dash(request):
    return render(request, 'pages/post_attend_dash.html')

def post_valid_dash(request):
    return render(request, 'pages/post_valid_dash.html')

def form_aricle_dash(request):
    return render(request, 'pages/form_aricle_dash.html')

def form_profil_dash(request):
    return render(request, 'pages/form_profil_dash.html')

def project_detail_dash(request):
    return render(request, 'pages/project_detail_dash.html')

def tables_dash(request):
    return render(request, 'pages/tables_dash.html')
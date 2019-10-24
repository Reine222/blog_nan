from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def category(request):
    return render(request, 'pages/category.html')

def element(request):
    return render(request, 'pages/element.html')

def archive(request):
    return render(request, 'pages/archive.html')

def single(request):
    return render(request, 'pages/single.html')
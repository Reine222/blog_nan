from django.shortcuts import render
from django.contrib.auth.context_processors.auth import RequestContext
# Create your views here.

def initialisation(request):
    return render(request, 'pages/index.html', context=RequestContext(request))

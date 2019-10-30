"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:id>/categorie/', views.selectCat, name="selectedcat"),
    path('category', views.category, name="category"),
    path('archive', views.archive, name="archive"),
    path('<int:pk>/single/', views.single, name="single"),
    path('inscription',views.register,name='inscription'),
    path('connect',views.connect, name="connect"),
    path('confirmer/', views.confirmer, name= 'confirmer'),
    path('confirmation/', views.confirm, name= 'confirmation'),
    path('comment/', views.comment, name='comment')
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_dash, name='index_dash'),
    path('tables_dash/', views.tables_dash, name='tables_dash'),
    path('<int:pk>/project_detail_dash/', views.project_detail_dash, name='project_detail_dash'),
    path('admin_visiteur_dash/', views.admin_visiteur_dash, name='admin_visiteur_dash'),
    path('detail_visiteur_dash', views.detail_visiteur_dash, name='detail_visiteur_dash'),
    path('page_dash/', views.page_dash, name='page_dash'),
    path('post_attend_dash/', views.post_attend_dash, name='post_attend_dash'),
    path('post_partage_dash/', views.post_partage_dash, name='post_partage_dash'),
    path('post_valid_dash/', views.post_valid_dash, name='post_valid_dash'),
    path('form_article_dash/', views.form_article_dash, name='form_article_dash'),
    path('form_profil_dash/', views.form_profil_dash, name='form_profil_dash')
    path('profil_visiteur_dash/', views.profil_visiteur_dash, name='profil_visiteur_dash'),
    
    path('tables_visiteur_dash/', views.tables_visiteur_dash, name='tables_visiteur_dash'),
]
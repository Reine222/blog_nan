from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_dash, name='index_dash'),
    path('page_dash/', views.page_dash, name='page_dash'),
    path('post_attend_dash/', views.post_attend_dash, name='post_attend_dash'),
    path('post_valid_dash/', views.post_valid_dash, name='post_valid_dash'),
    path('form_aricle_dash/', views.form_aricle_dash, name='form_aricle_dash'),
    path('form_profil_dash/', views.form_profil_dash, name='form_profil_dash'),
    path('project_detail_dash/', views.project_detail_dash, name='project_detail_dash'),
    path('tables_dash/', views.tables_dash, name='tables_dash'),
]
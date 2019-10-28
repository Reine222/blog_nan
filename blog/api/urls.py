from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewset import *

router = DefaultRouter()
router.register('category', CategoryViewset, base_name= 'category')
router.register('article', ArticleViewset, base_name= 'article')
router.register('commentaire', CommentaireViewset, base_name= 'commentaire')
router.register('profile', ProfileViewset, base_name= 'profile')
router.register('contact', ContactViewset, base_name= 'contact')
router.register('newsletter', NewsletterViewset, base_name= 'newsletter')
urlpatterns = [
    #...
]

urlpatterns += router.urls

import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from contact.models import *
from blogger.models import *
# Create a GraphQL type for the actor model

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

# Create a GraphQL type for the movie model
class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        


class CommentaireType(DjangoObjectType):
    class Meta:
        model = Commentaire

# Create a GraphQL type for the movie model
class ContactType(DjangoObjectType):
    class Meta:
        model = Contact


class NewsletterType(DjangoObjectType):
    class Meta:
        model = Newsletter


class Query(ObjectType):
    profile= graphene.Field(ProfileType, id=graphene.Int())
    profiles= graphene.List(ProfileType)
    
    category= graphene.Field(CategoryType, id=graphene.Int())
    categorie= graphene.List(CategoryType)
    
    articles = graphene.Field(ArticleType, id=graphene.Int())
    article = graphene.List(ArticleType)
    
    
    
    commentaire = graphene.Field(CommentaireType, id=graphene.Int())
    commentaires = graphene.List(CommentaireType)
    
    
    
    contact = graphene.Field(ContactType, id=graphene.Int())
    contacts= graphene.List(ContactType)
    
    newsletter= graphene.Field(NewsletterType, id=graphene.Int())
    newsletters= graphene.List(NewsletterType)



    def resolve_profile(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Profile.objects.get(pk=id)
        return None
    
    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.all()





    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Category.objects.get(pk=id)
        return None
    
    def resolve_categorie(self, info, **kwargs):
        return Category.objects.all()
    
    
    
    
    
    def resolve_articles(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Article.objects.get(pk=id)

        return None

    def resolve_article(self, info, **kwargs):
        return Article.objects.all()
    
    
    
    

    def resolve_contact(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Contact.objects.get(pk=id)

        return None
    
    def resolve_contacts(self, info, **kwargs):
        return Contact.objects.all()
    
    
    
    
    def resolve_newsletter(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Newsletter.objects.get(pk=id)

        return None
    
    def resolve_newsletters(self, info, **kwargs):
        return Newsletter.objects.all()



class ProfileInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    name = graphene.String()
    name = graphene.String()
    name = graphene.String()
    name = graphene.String()
    name = graphene.String()
    name = graphene.String()


class CategorieInput(graphene.InputObjectType):
    id = graphene.ID()
    nom = graphene.String()
    statut = graphene.String()
    date_add= graphene.String()
    date_up = graphene.String()
    

class ArticleInput(graphene.InputObjectType):
    id = graphene.ID()
    titre = graphene.String()
    image= graphene.String()
    description= graphene.String()
    titre = graphene.String()
    titre = graphene.String()
    categorie = graphene.List(ActorInput)

class CommentaireInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    actors = graphene.List(ActorInput)
    year = graphene.Int()

class ContactInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    actors = graphene.List(ActorInput)
    year = graphene.Int()

class NewsletterInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    actors = graphene.List(ActorInput)
    year = graphene.Int()
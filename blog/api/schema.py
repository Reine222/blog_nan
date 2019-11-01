import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from graphene import Field, String, List, Int


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
    fonction = graphene.String()
    image = graphene.String()
    description = graphene.String()
    statut = graphene.String()
    fb_lien = graphene.String()
    tweet_lien = graphene.String()
    ball_lien = graphene.String()
    Be_lien = graphene.String()
    user = graphene.String()
    contact = graphene.String()
    valider = graphene.String()
    


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    nom = graphene.String()
    statut = graphene.Boolean()
    date_add= graphene.String()
    date_up = graphene.String()
    

class ArticleInput(graphene.InputObjectType):
    id = graphene.ID()
    categorie1 = graphene.Int()
    titre = graphene.String()
    image= graphene.String()
    description= graphene.String()
    content = graphene.String()
    date = graphene.String()
    date_add = graphene.String()
    date_up = graphene.String()
    statut = graphene.Boolean()
    valider = graphene.Boolean()
    

class CommentaireInput(graphene.InputObjectType):
    id = graphene.ID()
    nom = graphene.String()
    article_id = graphene.Int()
    email = graphene.String()
    date = graphene.String()
    sujet = graphene.String()
    message = graphene.String()
    photo = graphene.String()
    date_add = graphene.String()
    date_up = graphene.String()
    statut = graphene.Boolean()
    


class ContactInput(graphene.InputObjectType):
    id = graphene.ID()
    nom = graphene.String()
    email = graphene.String()
    sujet = graphene.String()
    message = graphene.String()
    date_add = graphene.String()

class NewsletterInput(graphene.InputObjectType):
    id = graphene.ID()
    email = graphene.String()
    date_add = graphene.String()
    date_up = graphene.String()





class CreateProfile(graphene.Mutation):
    class Arguments:
        input = ProfileInput(required=True)

    ok = graphene.Boolean()
    profile = graphene.Field(ProfileType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        profile_instance = Profile(
            fonction = input.fonction,
            image = input.image,
            description = input.description,
            statut = input.statut,
            fb_lien = input.fb_lien,
            tweet_lien = input.tweet_lien,
            ball_lien = input.ball_lien,
            Be_lien = input.Be_lien,
            user = input.user,
            contact = input.contact,
            valider = input.valider,
            )
        profile_instance.save()
        return CreateProfile(ok=ok, profile=profile_instance)



class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        category_instance = Category(
            nom = input.nom,
            statut = input.statut,
            date_add= input.date_add,
            date_up = input.date_up,                      
            )
        category_instance.save()
        return CreateCategory(ok=ok, category=category_instance)





class CreateArticle(graphene.Mutation):
    class Arguments:
        input = ArticleInput(required=False)
        

    ok = graphene.Boolean()
    articles = graphene.Field(ArticleType)

    @staticmethod
    def mutate(root, info, categorie_id, input=None):
        ok = True    
        categorie = Category.objects.get(id=categorie1)
        articles_instance = (Article(
                categorie=input.categorie,
                titre = input.titre,
                image= input.image,
                description= input.description,
                content = input.content,
                date = input.date,
                date_add = input.date_add,
                date_up = input.date_up,
                statut = input.statut,
                valider = input.valider,
        ),)
        articles_instance.save()
        return CreateArticle(ok=ok, articles=articles_instance)





class CreateCommentaire(graphene.Mutation):
    class Arguments:
        input = CommentaireInput(required=True)

    ok = graphene.Boolean()
    commentaire = graphene.Field(CommentaireType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        article = Article.objects.get(id=article_id)
        commentaire_instance = Commentaire(
                nom = input.nom,
                article=input.article_id,
                email = input.email,
                date = input.date,
                sujet = input.sujet,
                message = input.message,
                photo = input.photo,
                date_add = input.date_add,
                date_up = input.date_up,
                statut = input.statut,
        )
        commentaire_instance.save()
        return CreateCommentaire(ok=ok, commentaire=commentaire_instance)








class CreateContact(graphene.Mutation):
    class Arguments:
        input = ContactInput(required=True)

    ok = graphene.Boolean()
    contact = graphene.Field(ContactType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        contact_instance = Contact(
            nom = input.nom,
            email = input.email,
            sujet = input.sujet,
            message = input.message,
            date_add = input.date_add,
            )
        
        
        contact_instance.save()
        return CreateContact(ok=ok, contact=contact_instance)

class UpdateContact(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ContactInput(required=True)

    ok = graphene.Boolean()
    contact = graphene.Field(ContactType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        contact_instance = Contact.objects.get(pk=id)
        if contact_instance:
            ok = True
            contact_instance.nom = input.nom
            contact_instance.email = input.email
            contact_instance.sujet = input.sujet
            contact_instance.message = input.message
            contact_instance.date_add = input.date_add
            
            contact_instance.save()
            return UpdateContact(ok=ok, contact=contact_instance)
        return UpdateContact(ok=ok, contact=None)





class CreateNewsletter(graphene.Mutation):
    class Arguments:
        input = NewsletterInput(required=True)

    ok = graphene.Boolean()
    newsletter = graphene.Field(NewsletterType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        newsletter_instance = Newsletter(
            email = input.email,
            date_add = input.date_add,
            date_up = input.date_up,
            )
        newsletter_instance.save()
        return CreateNewsletter(ok=ok, newsletter=newsletter_instance)

class UpdateNewsletter(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = NewsletterInput(required=True)

    ok = graphene.Boolean()
    newsletter = graphene.Field(NewsletterType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        newsletter_instance = Newsletter.objects.get(pk=id)
        if newsletter_instance:
            ok = True
            newsletter_instance.email = input.email
            newsletter_instance.date_add = input.date_add
            newsletter_instance.date_up = input.date_up
            
            newsletter_instance.save()
            return UpdateNewsletter(ok=ok, newsletter=newsletter_instance)
        return UpdateNewsletter(ok=ok, newsletter=None)






class Mutation(graphene.ObjectType):
    create_profile = CreateProfile.Field()
    
    create_category = CreateCategory.Field()
    
    create_articles = CreateArticle.Field()
    
    create_commentaire = CreateCommentaire.Field()
    
    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    
    create_newsletter = CreateNewsletter.Field()
    update_newsletter = UpdateNewsletter.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
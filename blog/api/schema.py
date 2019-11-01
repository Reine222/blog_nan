# import graphene
# from graphene_django.types import DjangoObjectType, ObjectType


# from contact.models import *
# from blogger.models import *
# # Create a GraphQL type for the actor model

# class ProfileType(DjangoObjectType):
#     class Meta:
#         model = Profile
        
# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category

# # Create a GraphQL type for the movie model
# class ArticleType(DjangoObjectType):
#     class Meta:
#         model = Article
        


# class CommentaireType(DjangoObjectType):
#     class Meta:
#         model = Commentaire

# # Create a GraphQL type for the movie model
# class ContactType(DjangoObjectType):
#     class Meta:
#         model = Contact


# class NewsletterType(DjangoObjectType):
#     class Meta:
#         model = Newsletter


# class Query(ObjectType):
#     profile= graphene.Field(ProfileType, id=graphene.Int())
#     profiles= graphene.List(ProfileType)
    
#     category= graphene.Field(CategoryType, id=graphene.Int())
#     categorie= graphene.List(CategoryType)
    
#     articles = graphene.Field(ArticleType, id=graphene.Int())
#     article = graphene.List(ArticleType)
    
    
    
#     commentaire = graphene.Field(CommentaireType, id=graphene.Int())
#     commentaires = graphene.List(CommentaireType)
    
    
    
#     contact = graphene.Field(ContactType, id=graphene.Int())
#     contacts= graphene.List(ContactType)
    
#     newsletter= graphene.Field(NewsletterType, id=graphene.Int())
#     newsletters= graphene.List(NewsletterType)



#     def resolve_profile(self, info, **kwargs):
#         id = kwargs.get('id')

#         if id is not None:
#             return Profile.objects.get(pk=id)
#         return None
    
#     def resolve_profiles(self, info, **kwargs):
#         return Profile.objects.all()





#     def resolve_category(self, info, **kwargs):
#         id = kwargs.get('id')

#         if id is not None:
#             return Category.objects.get(pk=id)
#         return None
    
#     def resolve_categorie(self, info, **kwargs):
#         return Category.objects.all()
    
    
    
    
    
#     def resolve_articles(self, info, **kwargs):
#         id = kwargs.get('id')

#         if id is not None:
#             return Article.objects.get(pk=id)

#         return None

#     def resolve_article(self, info, **kwargs):
#         return Article.objects.all()
    
    
    
    

#     def resolve_contact(self, info, **kwargs):
#         id = kwargs.get('id')

#         if id is not None:
#             return Contact.objects.get(pk=id)

#         return None
    
#     def resolve_contacts(self, info, **kwargs):
#         return Contact.objects.all()
    
    
    
    
#     def resolve_newsletter(self, info, **kwargs):
#         id = kwargs.get('id')

#         if id is not None:
#             return Newsletter.objects.get(pk=id)

#         return None
    
#     def resolve_newsletters(self, info, **kwargs):
#         return Newsletter.objects.all()



# class ProfileInput(graphene.InputObjectType):
#     id = graphene.ID()
#     fonction = graphene.String()
#     image = graphene.String()
#     description = graphene.String()
#     statut = graphene.String()
#     fb_lien = graphene.String()
#     tweet_lien = graphene.String()
#     ball_lien = graphene.String()
#     Be_lien = graphene.String()
#     user = graphene.String()
#     contact = graphene.String()
#     valider = graphene.String()
    




# class CategoryInput(graphene.InputObjectType):
#     id = graphene.ID()
#     nom = graphene.String()
#     statut = graphene.Boolean()
#     date_add= graphene.String()
#     date_up = graphene.String()
    

# class ArticleInput(graphene.InputObjectType):
#     id = graphene.ID()
#     titre = graphene.String()
#     image= graphene.String()
#     description= graphene.String()
#     content = graphene.String()
#     date = graphene.String()
#     date_add = graphene.String()
#     date_up = graphene.String()
#     statut = graphene.Boolean()
#     valider = graphene.Boolean()
#     categorie = graphene.List(CategoryInput)

# class CommentaireInput(graphene.InputObjectType):
#     id = graphene.ID()
#     nom = graphene.String()
#     article = graphene.List(ArticleInput)
#     email = graphene.String()
#     date = graphene.String()
#     sujet = graphene.String()
#     message = graphene.String()
#     photo = graphene.String()
#     date_add = graphene.String()
#     date_up = graphene.String()
#     statut = graphene.Boolean()
    

# class ContactInput(graphene.InputObjectType):
#     id = graphene.ID()
#     nom = graphene.String()
#     email = graphene.String()
#     sujet = graphene.String()
#     message = graphene.String()
#     date_add = graphene.String()

# class NewsletterInput(graphene.InputObjectType):
#     id = graphene.ID()
#     email = graphene.String()
#     date_add = graphene.String()
#     date_up = graphene.String()





# class CreateProfile(graphene.Mutation):
#     class Arguments:
#         input = ProfileInput(required=True)

#     ok = graphene.Boolean()
#     profile = graphene.Field(ProfileType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         ok = True
#         profile_instance = Profile(
#             fonction = input.fonction,
#             image = input.image,
#             description = input.description,
#             statut = input.statut,
#             fb_lien = input.fb_lien,
#             tweet_lien = input.tweet_lien,
#             ball_lien = input.ball_lien,
#             Be_lien = input.Be_lien,
#             user = input.user,
#             contact = input.contact,
#             valider = input.valider,
#             )
#         profile_instance.save()
#         return CreateProfile(ok=ok, profile=profile_instance)

# class UpdateProfile(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = ProfileInput(required=True)

#     ok = graphene.Boolean()
#     profile = graphene.Field(ProfileType)

#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = False
#         profile_instance = Profile.objects.get(pk=id)
#         if profile_instance:
#             ok = True
#             profile_instance.fonction = input.fonction
#             profile_instance.image = input.image
#             profile_instance.description = input.description
#             profile_instance.statut = input.statut
#             profile_instance.fb_lien = input.fb_lien
#             profile_instance.tweet_lien = input.tweet_lien
#             profile_instance.ball_lien = input.ball_lien
#             profile_instance.Be_lien = input.Be_lien
#             profile_instance.user = input.user
#             profile_instance.contact = input.contact
#             profile_instance.valider = input.valider
            
            
#             profile_instance.save()
#             return UpdateProfile(ok=ok, profile=profile_instance)
#         return UpdateProfile(ok=ok, profile=None)
    



# class CreateCategory(graphene.Mutation):
#     class Arguments:
#         input = CategoryInput(required=True)

#     ok = graphene.Boolean()
#     category = graphene.Field(CategoryType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         ok = True
#         category_instance = Category(
#             nom = input.nom,
#             statut = input.statut,
#             date_add= input.date_add,
#             date_up = input.date_up,                      
#             )
#         category_instance.save()
#         return CreateCategory(ok=ok, category=category_instance)

# class UpdateCategory(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = CategoryInput(required=True)

#     ok = graphene.Boolean()
#     category = graphene.Field(CategoryType)

#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = False
#         category_instance = Category.objects.get(pk=id)
#         if category_instance:
#             ok = True
#             category_instance.nom = input.nom
#             category_instance.statut = input.statut
#             category_instance.date_add= input.date_add
#             category_instance.date_up = input.date_up
            
#             category_instance.save()
#             return UpdateCategory(ok=ok, category=category_instance)
#         return UpdateCategory(ok=ok, category=None)
    
    




# class CreateArticle(graphene.Mutation):
#     class Arguments:
#         input = ArticleInput(required=True)

#     ok = graphene.Boolean()
#     articles = graphene.Field(ArticleType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         ok = True
#         categorie = []
#         for category_input in input.categorie:
#             category = Category.objects.get(pk=category_input.id)
#             if category is None:
#                 return CreateArticle(ok=False, movie=None)
#             categorie.append(category)
#             articles_instance = Article(
#                 titre = input.titre,
#                 image= input.image,
#                 description= input.description,
#                 content = input.content,
#                 date = input.date,
#                 date_add = input.date_add,
#                 date_up = input.date_up,
#                 statut = input.statut,
#                 valider = input.valider,
#             )
#         articles_instance.save()
#         articles_instance.categorie.set(categorie)
#         return CreateArticle(ok=ok, articles=articles_instance)


# class UpdateArticle(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = ArticleInput(required=True)

#     ok = graphene.Boolean()
#     articles = graphene.Field(ArticleType)

#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = False
#         articles_instance = Article.objects.get(pk=id)
#         if articles_instance:
#             ok = True
#             categorie = []
#             for category_input in input.categorie:
#                 category = Category.objects.get(pk=category_input.id)
#                 if category is None:
#                     return UpdateArticle(ok=False, articles=None)
#                 categorie.append(category)
#                 articles_instance.titre=input.titre
#                 articles_instance.image=input.image
#                 articles_instance.description=input.description
#                 articles_instance.content=input.content
#                 articles_instance.date=input.date
#                 articles_instance.date_add=input.date_add
#                 articles_instance.date_up=input.date_up
#                 articles_instance.statut=input.statut
#                 articles_instance.valider=input.valider
            
#                 articles_instance.categorie.set(categorie)
#             return UpdateArticle(ok=ok, articles=articles_instance)
#         return UpdateArticle(ok=ok, articles=None)












# class CreateCommentaire(graphene.Mutation):
#     class Arguments:
#         input = CommentaireInput(required=True)

#     ok = graphene.Boolean()
#     commentaire = graphene.Field(CommentaireType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         ok = True
#         article = []
#         for articles_input in input.article:
#             articles = Article.objects.get(pk=articles_input.id)
#             if articles is None:
#                 return CreateCommentaire(ok=False, commentaire=None)
#             article.append(articles)
#             commentaire_instance = Commentaire(
#                 nom = input.nom,
#                 email = input.email,
#                 date = input.date,
#                 sujet = input.sujet,
#                 message = input.message,
#                 photo = input.photo,
#                 date_add = input.date_add,
#                 date_up = input.date_up,
#                 statut = input.statut,
#             )
#         commentaire_instance.save()
#         commentaire_instance.article.set(article)
#         return CreateCommentaire(ok=ok, commentaire=commentaire_instance)


# class UpdateCommentaire(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = CommentaireInput(required=True)

#     ok = graphene.Boolean()
#     commentaire = graphene.Field(CommentaireType)

#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = False
#         commentaire_instance = Commentaire.objects.get(pk=id)
#         if commentaire_instance:
#             ok = True
#             article = []
#             for articles_input in input.article:
#                 articles = Article.objects.get(pk=articles_input.id)
#                 if articles is None:
#                     return UpdateCommentaire(ok=False, commentaire=None)
#                 article.append(articles)
                
#                 commentaire_instance.nom=input.nom
#                 commentaire_instance.email=input.email
#                 commentaire_instance.date=input.date
#                 commentaire_instance.sujet=input.sujet
#                 commentaire_instance.message=input.title
#                 commentaire_instance.photo=input.photo
#                 commentaire_instance.date_add=input.date_add
#                 commentaire_instance.date_up=input.date_up
#                 commentaire_instance.statut=input.statut
            
            
#                 commentaire_instance.article.set(article)
#             return UpdateCommentaire(ok=ok, commentaire=commentaire_instance)
#         return UpdateCommentaire(ok=ok, commentaire=None)

















# class CreateContact(graphene.Mutation):
#     class Arguments:
#         input = ContactInput(required=True)

#     ok = graphene.Boolean()
#     contact = graphene.Field(ContactType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         ok = True
#         contact_instance = Contact(
#             nom = input.nom,
#             email = input.email,
#             sujet = input.sujet,
#             message = input.message,
#             date_add = input.date_add,
#             )
        
        
#         contact_instance.save()
#         return CreateContact(ok=ok, contact=contact_instance)

# class UpdateContact(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = ContactInput(required=True)

#     ok = graphene.Boolean()
#     contact = graphene.Field(ContactType)

#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = False
#         contact_instance = Contact.objects.get(pk=id)
#         if contact_instance:
#             ok = True
#             contact_instance.nom = input.nom
#             contact_instance.email = input.email
#             contact_instance.sujet = input.sujet
#             contact_instance.message = input.message
#             contact_instance.date_add = input.date_add
            
#             contact_instance.save()
#             return UpdateContact(ok=ok, contact=contact_instance)
#         return UpdateContact(ok=ok, contact=None)





# class CreateNewsletter(graphene.Mutation):
#     class Arguments:
#         input = NewsletterInput(required=True)

#     ok = graphene.Boolean()
#     newsletter = graphene.Field(NewsletterType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         ok = True
#         newsletter_instance = Newsletter(
#             email = input.email,
#             date_add = input.date_add,
#             date_up = input.date_up,
#             )
#         newsletter_instance.save()
#         return CreateNewsletter(ok=ok, newsletter=newsletter_instance)

# class UpdateNewsletter(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required=True)
#         input = NewsletterInput(required=True)

#     ok = graphene.Boolean()
#     newsletter = graphene.Field(NewsletterType)

#     @staticmethod
#     def mutate(root, info, id, input=None):
#         ok = False
#         newsletter_instance = Newsletter.objects.get(pk=id)
#         if newsletter_instance:
#             ok = True
#             newsletter_instance.email = input.email
#             newsletter_instance.date_add = input.date_add
#             newsletter_instance.date_up = input.date_up
            
#             newsletter_instance.save()
#             return UpdateNewsletter(ok=ok, newsletter=newsletter_instance)
#         return UpdateNewsletter(ok=ok, newsletter=None)






# class Mutation(graphene.ObjectType):
#     create_profile = CreateProfile.Field()
#     update_profile = UpdateProfile.Field()
    
#     create_category = CreateCategory.Field()
#     update_category = UpdateCategory.Field()
    
#     create_articles = CreateArticle.Field()
#     update_articles = UpdateArticle.Field()
    
#     create_commentaire = CreateCommentaire.Field()
#     update_commentaire = UpdateCommentaire.Field()
    
#     create_contact = CreateContact.Field()
#     update_contact = UpdateContact.Field()
    
#     create_newsletter = CreateNewsletter.Field()
#     update_newsletter = UpdateNewsletter.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
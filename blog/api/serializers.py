from rest_framework import serializers

from contact.models import *
from blogger.models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        deph = 1

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        deph = 1


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, required=False)

    class Meta:
        model = Article
        fields = '__all__'
        deph = 1


class CommentaireSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Commentaire
        fields = '__all__'
        deph = 1

class ContactSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Contact
        fields = '__all__'
        deph = 1

class NewsletterSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Newsletter
        fields = '__all__'
        deph = 1
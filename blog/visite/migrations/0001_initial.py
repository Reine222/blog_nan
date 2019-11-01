# Generated by Django 2.2.6 on 2019-11-01 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('date', models.DateField(auto_now_add=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_up', models.DateTimeField(auto_now=True)),
                ('statut', models.BooleanField(default=True)),
                ('valider', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('statut', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_up', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('pays', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('continent', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('reseau', models.CharField(max_length=50)),
                ('page', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserVisiteur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.IntegerField()),
                ('articl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArticleLike', to='visite.Article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('date', models.DateTimeField()),
                ('sujet', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('photo', models.ImageField(default='images/user.jpg', upload_to='images')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_up', models.DateTimeField(auto_now=True)),
                ('statut', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArticleCommentaire', to='visite.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_cat', to='visite.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Articleuser_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 2.2.6 on 2019-11-01 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='article',
        ),
        migrations.AlterField(
            model_name='like',
            name='articl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArticleLike', to='blogger.Article'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
    ]

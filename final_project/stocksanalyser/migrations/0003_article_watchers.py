# Generated by Django 3.1.6 on 2021-04-24 19:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocksanalyser', '0002_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='watchers',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
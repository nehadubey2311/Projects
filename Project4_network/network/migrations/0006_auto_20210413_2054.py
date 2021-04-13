# Generated by Django 3.1.6 on 2021-04-13 20:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20210408_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(related_name='_user_follows_+', to=settings.AUTH_USER_MODEL),
        ),
    ]

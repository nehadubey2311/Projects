# Generated by Django 3.1.6 on 2021-03-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20210307_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_image',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]

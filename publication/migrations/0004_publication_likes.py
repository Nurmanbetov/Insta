# Generated by Django 3.1.1 on 2020-09-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0003_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Нравится'),
        ),
    ]

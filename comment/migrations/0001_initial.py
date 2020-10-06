# Generated by Django 3.1.1 on 2020-10-06 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publication', '0006_remove_publication_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('text', models.TextField()),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='publication.publication', verbose_name='Публикация')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentToComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('text', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='comment.comment', verbose_name='На комментарий')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_comment', to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentToCommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='comment.commenttocomment', verbose_name='Какому комментарию (на комментарий)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_comment_like', to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('commnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='comment.comment', verbose_name='Какой публикации')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

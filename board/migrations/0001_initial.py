# Generated by Django 3.0.8 on 2020-09-17 11:51

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False, verbose_name='글 번호')),
                ('head', models.CharField(choices=[('N', '자유'), ('Q', '질문'), ('I', '정보')], max_length=16)),
                ('title', models.CharField(max_length=126)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('author', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('rcmd', models.IntegerField(default=0)),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

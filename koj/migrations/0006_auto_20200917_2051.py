# Generated by Django 3.0.8 on 2020-09-17 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koj', '0005_merge_20200917_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.DeleteModel(
            name='Fortest',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

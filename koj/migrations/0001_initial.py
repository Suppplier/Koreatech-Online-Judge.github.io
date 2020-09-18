# Generated by Django 3.1.1 on 2020-09-17 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import koj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('contest_id', models.AutoField(primary_key=True, serialize=False, verbose_name='대회번호')),
                ('title', models.CharField(max_length=128)),
                ('winner', models.CharField(blank=True, max_length=128, null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_id', models.IntegerField(unique=True, verbose_name='문제 번호')),
                ('title', models.CharField(max_length=256, verbose_name='제목')),
                ('body', models.TextField()),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('time_limit', models.IntegerField(default=1)),
                ('memory_limit', models.IntegerField(default=128)),
                ('made_by', models.CharField(default='admin', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.FileField(upload_to=koj.models.prob_path)),
                ('output_data', models.FileField(upload_to=koj.models.prob_path)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koj.problem')),
            ],
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.IntegerField()),
                ('code', models.TextField()),
                ('length', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('result', models.IntegerField(null=True)),
                ('memory', models.IntegerField(null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koj.problem')),
            ],
        ),
        migrations.CreateModel(
            name='ConProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koj.contest')),
                ('problems', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koj.problem')),
            ],
        ),
        migrations.CreateModel(
            name='ConParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koj.contest')),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

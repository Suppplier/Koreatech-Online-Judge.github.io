# Generated by Django 3.0.8 on 2020-09-25 08:52

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
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='언어')),
                ('filename', models.CharField(default='', max_length=32, verbose_name='파일명')),
                ('compile_option', models.CharField(default='', max_length=256, verbose_name='컴파일 옵션')),
                ('exe', models.CharField(default='', max_length=32, verbose_name='실행 바이너리')),
                ('args', models.CharField(blank=True, default='', max_length=256, verbose_name='명령 인수')),
            ],
            options={
                'verbose_name_plural': '언어',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_id', models.IntegerField(unique=True, verbose_name='문제 번호')),
                ('title', models.CharField(max_length=256, verbose_name='제목')),
                ('body', models.TextField(verbose_name='본문')),
                ('input', models.TextField(verbose_name='입력')),
                ('output', models.TextField(verbose_name='출력')),
                ('time_limit', models.IntegerField(default=1, verbose_name='시간 제한 (초)')),
                ('memory_limit', models.IntegerField(default=128, verbose_name='메모리 제한 (MB)')),
                ('made_by', models.CharField(default='admin', max_length=32, verbose_name='작성자')),
                ('is_closed', models.BooleanField(default=False, verbose_name='비공개 여부')),
            ],
            options={
                'verbose_name_plural': '문제',
            },
        ),
        migrations.CreateModel(
            name='Testcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.FileField(upload_to=koj.models.prob_path, verbose_name='입력 데이터')),
                ('output_data', models.FileField(upload_to=koj.models.prob_path, verbose_name='정답 데이터')),
                ('is_example', models.BooleanField(default=False, verbose_name='예시로 사용')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koj.Problem')),
            ],
            options={
                'verbose_name_plural': '테스트케이스',
            },
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(verbose_name='코드')),
                ('length', models.IntegerField(verbose_name='길이')),
                ('time', models.DateTimeField(verbose_name='제출 시간')),
                ('result', models.IntegerField(choices=[(0, 'Ac'), (1, 'Wa'), (2, 'Tle'), (3, 'Mle'), (4, 'Ole'), (5, 'Ce'), (6, 'Re'), (7, 'Er'), (8, 'Ing')], null=True, verbose_name='결과')),
                ('memory', models.IntegerField(null=True, verbose_name='메모리')),
                ('runtime', models.IntegerField(null=True, verbose_name='시간')),
                ('for_contest', models.BooleanField(default=False, verbose_name='대회용 제출')),
                ('contest_id', models.IntegerField(null=True, verbose_name='대회 번호')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='koj.Language', verbose_name='언어')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koj.Problem')),
            ],
            options={
                'verbose_name_plural': '제출 이력',
            },
        ),
    ]

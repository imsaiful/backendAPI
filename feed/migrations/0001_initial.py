# Generated by Django 2.1.7 on 2019-04-18 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anchor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('channel_name', models.CharField(max_length=200)),
                ('wiki', models.TextField()),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Dna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Firstpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Hindustan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='IndexTop10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_keyword', models.TextField()),
                ('db_frequency', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Indianexpress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Indiatoday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Ndtv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='News18',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='News_Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('info', models.TextField()),
                ('image', models.FileField(upload_to='')),
                ('website', models.TextField()),
                ('total_star', models.PositiveIntegerField(default=0)),
                ('total_user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Oneindia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Republic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.News_Channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thehindu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Zeenews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.TextField()),
                ('link', models.TextField(unique=True)),
                ('date', models.TextField(default=django.utils.timezone.now)),
                ('category', models.TextField(null=True)),
                ('sentiment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='count',
            name='channelId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.News_Channel'),
        ),
        migrations.AddField(
            model_name='count',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

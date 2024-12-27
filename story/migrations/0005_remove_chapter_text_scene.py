# Generated by Django 4.2.7 on 2024-12-27 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_alter_story_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='text',
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('text', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenes', to='story.chapter')),
            ],
        ),
    ]
